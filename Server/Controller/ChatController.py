from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.ChatRequestModel import ChatIdGetRequest, SendChatRequest
from Server.Repository.ChatRepository import ChatRepository

###############################################################################

RepChat = ChatRepository()

###############################################################################

async def get_my_chat(body: ChatIdGetRequest):
    retVal = BaseOutputModel()
    try:
        q = {"$and":[
            {"userEmail":body.email}
        ]}
        curr = RepChat.GetOne(q)
        curr['_id'] = str(curr['_id'])
        retVal.status = 1
        retVal.message = "success"
        retVal.result = curr
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

    
async def send_chat(body: SendChatRequest):
    retVal = BaseOutputModel()
    try:
        q = {"$and":[
            {"userEmail":body.email}
        ]}
        curr = RepChat.GetOne(q)
        if curr == None:
            retVal.status=0
            retVal.message="chat not found"
            return retVal
        curr['_id'] = str(curr['_id'])
        chat_rows = list(curr["chats"])
        chat_rows.append(body.get_insert_json())
        update_q = { "$set":
            { "chats" : chat_rows }
        }
        RepChat.Update(q, update_q)
        retVal.message = "done"
        retVal.status = 1
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal