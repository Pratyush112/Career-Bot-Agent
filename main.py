import os
import json
from openai import OpenAI
from pypdf import PdfReader 
from dotenv import load_dotenv 
import requests 
import gradio as gr 
# from twilio.rest import Client

load_dotenv(override=True) 

geminiApi = os.getenv("GEMINI_API_KEY")
baseUrl = "https://generativelanguage.googleapis.com/v1beta/openai/"
pushUrl = "https://api.pushover.net/1/messages.json"

#created a function for the push notification using Twilio
def notification(message: str):
    print(f"Notification sent: {message}")
    payload = {"user":os.getenv("PUSHOVER_USER_KEY"), "token":os.getenv("PUSHOVER_API_TOKEN"), "message":message}
    return requests.post(pushUrl,data=payload)

    # twilioSid = os.getenv("TWILIO_ACCOUNT_SID")
    # twilioAuth = os.getenv("TWILIO_AUTH_TOKEN")
    # twilioFrom = os.getenv("TWILIO_FROM_NUMBER")
    # twilioTo = os.getenv("TWILIO_TO_NUMBER")

    # if not all([twilioSid, twilioAuth, twilioFrom, twilioTo]):
    #     print("Twilio credentials are missing please add credentials")
    #     print(f"SID: {twilioSid} \n\n FROM_NUMBER: {twilioFrom} \n\n TO_NUMBER: {twilioTo}")
    #     return None

    # client = Client(twilioSid, twilioAuth)
    # try:
    #     msg= client.messages.create(body = message, from_ = twilioFrom, to = twilioTo)
    #     print(f"[Twilio] SMS sent: {msg.sid}")
    #     return msg
    # except Exception as e:
    #     print(f"[Twilio Error]: {e}")
    #     return None 

#creating tools for the model    
def recordUserDetails(name, email, notes="Notes not provided"):
    notification(f"User Name: {name}, User Email: {email}, User Notes: {notes}")
    return {"Details Recorded Successfully":"ok"}

def recordUnknownQuestion(question):
    notification(f"Unknown Question: {question}")
    return {"Unknown Question Recorded Successfully":"ok"}

#creating a json for the toolss
userDetailsrecord_json= {
    "name":"recordUserDetails",
    "description":"This tool is used to record the user details and send a notification to the owner",
    "parameters":{   
        "type":"object",
        "properties":{
            "name":{
                "type":"string",
                "description":"The name of the user"
            },
            "email":{
                "type":"string",
                "description":"The email of the user"
            },
            "notes":{
                "type":"string",
                "description":"The notes of the user"
            },
        },
        "required":["name", "email"],
        "additionalProperties":False
    }
}

unknownQuestionrecord_json= {
    "name":"recordUnknownQuestion",
    "description":"This tool is used to record the unknown question and send a notification to the owner",
    "parameters":{
        "type":"object",
        "properties":{
            "question":{
                "type":"string",
                "description":"This is the question that chatbot will not be able to answer and send notification to the user."
            },
        },
        "required":["question"],
        "additionalProperties":False
    }
}

tools=[{"type":"function", "function":userDetailsrecord_json},
        {"type":"function", "function":unknownQuestionrecord_json}]

class chatbot:
    
    def __init__(self):
        self.name = "Pratyush Kumar Saha"
        self.linkedin = ""
        self.resume=""
        linkedin_profile = PdfReader("Profile/Profile.pdf")
        for page in linkedin_profile.pages:
            text=page.extract_text()
            if text:
                self.linkedin+=text
        
        readResume = PdfReader("Profile/Resume.pdf")
        for pg in readResume.pages:
            txt=pg.extract_text()
            if txt:
                self.resume+=txt
        
        with open("Profile/me.txt", "r", encoding="utf-8") as file:
            self.summary = file.read()

        self.gemini=OpenAI(api_key=geminiApi, base_url=baseUrl)

    def handleToolCalls(self, tool_calls):
        tool_message=[]
        for tool_call in tool_calls:    
            #calling the tool name
            tool_name=tool_call.function.name

            #calling arguements according to the tool
            arguments = json.loads(tool_call.function.arguments)

            #getting tool from python env
            tool = globals().get(tool_name)

            #gives the tool_message
            result=tool(**arguments) if tool else {None}
            #appending the tool message 
            tool_message.append({"role":"tool","content":json.dumps(result), "tool_call_id":tool_call.id})
        return tool_message

    def system_prompt(self):
        system_prompt = f"""You are acting as {self.name} in {self.name}'s website. \
                            Your responsibility is to answer question potentially based on {self.name}'s career, background and experience. \
                            Also your responsibility is to show {self.name} as faithfully and smart as possible. \
                            Be professional and engaging as if you are talking to a potential client or a recruiter or a future employee.\
                            You will be provided with {self.name}'s linkedin profile, resume and summary text file, refer them while answering the questions. \
                            If you do not know any answer, don't make your own answer, use your recordUnknownQuestion tool to record the question even if is not related to {self.name}'s background or career or if the question is trivial. \
                            If the user is engaging in the conversation, try to steer them to connect to {self.name} via email, ask their name and email and use your recordUserDetails tool to record the name and email. """

        system_prompt+=f"Here is {self.name}'s:\n\n Linkedin Profile: {self.linkedin} \n\n Resume : {self.resume} \n\n Summary: {self.summary} \n\n"
        system_prompt+=f"With this context talk to the user and always staying in character"

        return system_prompt

    def chat(self, message, history):
        msg = [{"role":"system", "content":self.system_prompt()}] + history + [{"role":"user", "content":message}]
        done = False
        while not done:
            response = self.gemini.chat.completions.create(
                model="gemini-2.5-flash",
                messages=msg,
                tools=tools
            )

            if response.choices[0].finish_reason=="tool_calls":
                message = response.choices[0].message
                tool_calls = message.tool_calls
                tool_message=self.handleToolCalls(tool_calls)
                msg.append(message)
                msg.extend(tool_message)
            else:
                done=True
        return response.choices[0].message.content

if __name__=="__main__":
    chatbot=chatbot()
    gr.ChatInterface(chatbot.chat).launch()

