from pydantic import BaseModel

class ChatRoom(BaseModel):
    cid:str
    userEmail:str
    chats:list(object)

    def get_chat_row(this):
        return list(this.chats)

    def get_chat_header(this):
        return {
            "cid":this.cid,
            "userEmail":this.userEmail,
        }

    def get_insert_json(this):
        return {
            "cid":this.cid,
            "userEmail":this.userEmail,
            "chats":this.chats
        }
    