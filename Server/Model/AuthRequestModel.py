from pydantic import BaseModel
from pydantic.networks import stricturl 

class ModelRegisterRequest(BaseModel):
    username:str
    email:str
    phone:str
    password:str

    def getInsertJson(this):
        return {
            "username":this.username,
            "email":this.email,
            "phone":this.phone,
            "password":this.password
        }
    
class ModelLoginRequest(BaseModel):
    username:str
    password:str
    
class ModelUserDetailRequest(BaseModel):
    username:str

class ModelUpdateUserEmailRequest(BaseModel):
    id:str
    username:str
    password:str
    updateEmail:str

class ModelUpdateUserPhoneRequest(BaseModel):
    id:str
    username:str
    password:str
    updatePhone:str

class ModelUpdateUserPasswordRequest(BaseModel):
    id:str
    username:str
    password:str
    updatePassword:str