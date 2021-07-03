## Package Import ##
from Server.Controller.ChatController import get_my_chat
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
## AppCode Import ##
from Server.Controller.TransactionController import *
from Server.Utility.JWT import JWTBearer

###############################################################################

TransactionRoute = APIRouter()

###############################################################################

@TransactionRoute.post("/transaction/insert")
async def insert_transaction(body: TransactionCreateRequestModel) -> BaseOutputModel:
    return await make_transaction(body);

@TransactionRoute.post("/transaction/get")
async def insert_transaction(body: TransactionGetRequestModel) -> BaseOutputModel:
    return await get_my_transaction(body);

@TransactionRoute.post("/transaction/getspecific")
async def insert_transaction(body: TransactionSpecificRequestMoodel) -> BaseOutputModel:
    return await get_specific_transaction(body)