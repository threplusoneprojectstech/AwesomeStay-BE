## Package Import ##
import os
from fastapi import APIRouter
from fastapi.param_functions import Depends
## AppCode Import ##
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Utility.JWT import JWTBearer

###############################################################################

MainRoute = APIRouter()

###############################################################################

@MainRoute.get("/")
async def root():
    retVal = BaseOutputModel()
    try:
        retVal.status = 1
        retVal.result = "hello there"
        return retVal;
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

@MainRoute.get("/clean")
async def clean():
    retVal = BaseOutputModel()
    try:
        os.system("pyclean . -q")
        retVal.status = 1
        retVal.result = "Pycache Cleaned"
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal
    
@MainRoute.get("/verifytoken", dependencies=[Depends(JWTBearer())])
async def verifytoken():
    retVal = BaseOutputModel()
    try:
        retVal.status = 1
        retVal.result = "Token is valid"
        return retVal;
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal