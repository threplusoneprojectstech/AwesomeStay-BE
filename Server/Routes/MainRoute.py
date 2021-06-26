import os
from fastapi import APIRouter, Body
from Server.Model.BaseOutputModel import BaseOutputModel

MainRoute = APIRouter()

@MainRoute.get("/")
async def root():
    retVal = BaseOutputModel()
    retVal.status = 1
    retVal.result = "hello there"
    return retVal;

@MainRoute.get("/clean")
async def clean():
    os.system("pyclean .")
    retVal = BaseOutputModel()
    retVal.status = 1
    retVal.result = "Pycache Cleaned"
    return retVal
