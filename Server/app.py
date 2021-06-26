from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Server.Routes.MainRoute import MainRoute
from Server.Routes.AuthRoute import AuthRoute
import os

os.system("pyclean .")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(MainRoute, tags=["Main"])
app.include_router(AuthRoute, tags=["Auth"])
