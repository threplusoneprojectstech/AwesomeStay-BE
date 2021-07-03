## Package Import ##
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
## AppCode Import ##
from Server.Controller.AdminController import *
from Server.Model.AdminRequestModel import *
from Server.Utility.JWT import JWTBearer

###############################################################################

AdminRoute = APIRouter()

###############################################################################

@AdminRoute.post("/admin/register")
async def register(body: ModelInsertRequest):
    return await admin_insert(body);

@AdminRoute.post("/admin/login")
async def login(body: ModelLoginRequest):
    return await admin_login(body)