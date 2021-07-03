## Package Import ##
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
## AppCode Import ##
from Server.Controller.AuthController import *
from Server.Model.AuthRequestModel import *
from Server.Utility.JWT import JWTBearer

###############################################################################

AuthRoute = APIRouter()

###############################################################################

@AuthRoute.post("/auth/register")
async def register(body: ModelRegisterRequest):
    return await auth_register(body);

@AuthRoute.post("/auth/login")
async def login(body: ModelLoginRequest):
    return await auth_login(body)

@AuthRoute.post("/auth/getdetails", dependencies=[Depends(JWTBearer())])
async def get_details(body: ModelUserDetailRequest):
    return await auth_user_details(body)

@AuthRoute.post("/auth/update/email", dependencies=[Depends(JWTBearer())])
async def update_email(body: ModelUpdateUserEmailRequest):
    return await auth_update_user_email(body)

@AuthRoute.post("/auth/update/phone", dependencies=[Depends(JWTBearer())])
async def update_phone(body: ModelUpdateUserPhoneRequest):
    return await auth_update_user_phone(body)

@AuthRoute.post("/auth/update/password", dependencies=[Depends(JWTBearer())])
async def update_password(body: ModelUpdateUserPasswordRequest):
    return await auth_update_user_password(body)

@AuthRoute.post("/auth/update/debit", dependencies=[Depends(JWTBearer())])
async def update_debit(body: ModelUpdateUserDebitRequest):
    return await auth_update_user_debit(body)