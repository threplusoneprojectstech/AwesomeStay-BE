from bson.objectid import ObjectId
from datetime import date
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.TransactionRequestModel import TransactionCreateRequestModel, TransactionGetRequestModel, TransactionSpecificRequestMoodel
from Server.Repository.TransactionRepository import TransactionRepository

###############################################################################

RepTrans = TransactionRepository()

###############################################################################

async def make_transaction(body:TransactionCreateRequestModel):
    retVal = BaseOutputModel()
    try:
        if RepTrans.Insert(body.get_insert_json()) == False:
            retVal.message = "failed inserting transaction"
            retVal.status = 0
            return retVal
        retVal.message = "transaction inserted"
        retVal.result = body.get_insert_json()
        retVal.status = 1
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal
    
###############################################################################

async def get_my_transaction(body:TransactionGetRequestModel):
    retVal = BaseOutputModel()
    try:
        q = { "$and":[
            {"email":body.email}
        ] }
        data = RepTrans.Get(q)
        if data == None:
            retVal.message = "data not found"
            retVal.status = 0
            return retVal
        retVal.result = []
        for i in data:
            i["_id"] = str(i["_id"])
            retVal.result.append(i)
        retVal.status = 1
        retVal.message = "success"
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal
    
###############################################################################

async def get_specific_transaction(body:TransactionSpecificRequestMoodel):
    retVal = BaseOutputModel()
    try:
        q = { "$and": [
            { "_id":ObjectId(body.id) }
        ]}
        data = RepTrans.GetOne(q)
        if data == None:
            retVal.message = "data not found"
            retVal.status = 0
            return retVal
        data["_id"] = str(data["_id"])
        retVal.status = 1
        retVal.message = "success"
        retVal.result = data
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal