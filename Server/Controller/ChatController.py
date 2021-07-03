from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.ChatRequestModel import ChatIdGetRequest, SendChatRequest
from Server.Repository.ChatRepository import ChatRepository

###############################################################################

RepChat = ChatRepository()

###############################################################################

async def chat_get(body: ChatIdGetRequest):
    retVal = BaseOutputModel()
    try:
        query = {"$and":[
            {"userEmail":body.email}
        ]}
        curr = RepChat.GetOne(query)

        curr['_id'] = str(curr['_id'])
        retVal.status = 1
        retVal.message = "success"
        retVal.result = curr
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

###############################################################################

async def chat_send(body: SendChatRequest):
    retVal = BaseOutputModel()
    try:
        query = {"$and":[
            {"userEmail":body.email}
        ]}
        curr = RepChat.GetOne(query)

        if curr == None:
            retVal.status=0
            retVal.message="chat not found"
            return retVal
        curr['_id'] = str(curr['_id'])
        chat_rows = list(curr["chats"])
        chat_rows.append(body.get_insert_json())
        update_data = { "$set":
            { "chats" : chat_rows }
        }
        RepChat.Update(query, update_data)
        retVal.message = "done"
        retVal.status = 1
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal