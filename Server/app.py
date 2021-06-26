from fastapi import FastAPI
from Server.Routes.MainRoute import MainRoute
from Server.Routes.AuthRoute import AuthRoute

app = FastAPI()

app.include_router(MainRoute, tags=["Main"])
app.include_router(AuthRoute, tags=["Auth"])