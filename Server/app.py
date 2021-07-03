## Package Import ##
import os
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
## AppCode Import ##
from Server.Routes.MainRoute import MainRoute
from Server.Routes.AuthRoute import AuthRoute
from Server.Routes.AdminRoute import AdminRoute

###############################################################################

os.system("pyclean . -q")
app = FastAPI()
security = HTTPBearer()

###############################################################################

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(MainRoute, tags=["Main"])
app.include_router(AuthRoute, tags=["Auth"])
app.include_router(AdminRoute, tags=["Admin"])