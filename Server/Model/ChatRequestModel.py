from pydantic import BaseModel
from datetime import datetime

class ChatIdGetRequest(BaseModel):
    email:str

class SendChatRequest(BaseModel):
    email:str
    message:str
    isUser:int

    def get_insert_json(this):
        return {
            "ts":datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "message":this.message,
            "isUser":this.message
        }