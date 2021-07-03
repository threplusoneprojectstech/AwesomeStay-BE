from Server.Controller.ChatController import get_my_chat, send_chat
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.ChatRequestModel import ChatIdGetRequest, SendChatRequest
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends

###############################################################################

ChatRouter = APIRouter()

###############################################################################

@ChatRouter.post("/chat/get")
async def insert_product(body: ChatIdGetRequest) -> BaseOutputModel:
    return await get_my_chat(body);

@ChatRouter.post("/chat/send")
async def insert_product(body: SendChatRequest) -> BaseOutputModel:
    return await send_chat(body);