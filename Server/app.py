from fastapi import FastAPI
from Server.Routes.MainRoute import MainRoute
from Server.Routes.AuthRoute import AuthRoute
import os

os.system("pyclean .")
app = FastAPI()

app.include_router(MainRoute, tags=["Main"])
app.include_router(AuthRoute, tags=["Auth"])
