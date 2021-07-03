from pydantic import BaseModel

class TransactionCreateRequestModel(BaseModel):
    email:str
    orders:list
    
    def get_insert_json(this):
        return {
            "email": this.email,
            "orders": this.orders
        }
    
class TransactionGetRequestModel(BaseModel):
    email:str