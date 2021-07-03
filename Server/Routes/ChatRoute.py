from Server.Controller.ChatController import chat_send, chat_get
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.ChatRequestModel import ChatIdGetRequest, SendChatRequest
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends

###############################################################################

ChatRouter = APIRouter()

###############################################################################

@ChatRouter.post("/chat/get")
async def insert_product(body: ChatIdGetRequest) -> BaseOutputModel:
    return await chat_get(body);

@ChatRouter.post("/chat/send")
async def insert_product(body: SendChatRequest) -> BaseOutputModel:
    return await chat_send(body);