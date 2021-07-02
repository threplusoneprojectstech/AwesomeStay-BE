## Package Import ##
import os
from fastapi import APIRouter, Body
## AppCode Import ##
from Server.Model.BaseOutputModel import BaseOutputModel

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
    
# @MainRoute.get("/token")
# async def token():
