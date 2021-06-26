from fastapi import APIRouter, Body
from Server.Controller.DatabaseController import initialize_database

from Server.Controller.AuthController import *
from Server.Model.AuthRequestModel import *


AuthRoute = APIRouter()
USER_COLLECTION = initialize_database("user")

@AuthRoute.post("/auth/register")
async def register(body: ModelRegisterRequest):
    return await auth_register(USER_COLLECTION, body);

@AuthRoute.get("/auth/login")
async def login(body: ModelLoginRequest):
    return await auth_login(USER_COLLECTION, body)

@AuthRoute.get("/auth/getdetails")
async def get_details(body: ModelUserDetailRequest):
    return await auth_user_details(USER_COLLECTION, body)

@AuthRoute.post("/auth/update/email")
async def update_email(body: ModelUpdateUserEmailRequest):
    return await auth_update_user_email(USER_COLLECTION, body)

@AuthRoute.post("/auth/update/phone")
async def update_email(body: ModelUpdateUserPhoneRequest):
    return await auth_update_user_phone(USER_COLLECTION, body)

@AuthRoute.post("/auth/update/password")
async def update_email(body: ModelUpdateUserPasswordRequest):
    return await auth_update_user_password(USER_COLLECTION, body)