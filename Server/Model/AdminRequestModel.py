from pydantic import BaseModel

class ModelInsertRequest(BaseModel):
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