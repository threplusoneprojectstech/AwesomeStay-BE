from pydantic import BaseModel

class ModelRegisterRequest(BaseModel):
    fullName:str
    email:str
    phone:str
    debit:str
    password:str

    def getInsertJson(this):
        return {
            "fullName":this.fullName,
            "email":this.email,
            "phone":this.phone,
            "debit":this.debit,
            "password":this.password
        }
    
class ModelLoginRequest(BaseModel):
    email:str
    password:str
    
class ModelUserDetailRequest(BaseModel):
    email:str

class ModelUpdateUserEmailRequest(BaseModel):
    id:str
    email:str
    password:str
    updateEmail:str

class ModelUpdateUserPhoneRequest(BaseModel):
    id:str
    email:str
    password:str
    updatePhone:str

class ModelUpdateUserPasswordRequest(BaseModel):
    id:str
    email:str
    password:str
    updatePassword:str

class ModelUpdateUserDebitRequest(BaseModel):
    id:str
    email:str
    password:str
    updateDebit:str
