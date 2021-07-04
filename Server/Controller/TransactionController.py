from bson.objectid import ObjectId
from datetime import date
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.TransactionRequestModel import TransactionCreateRequestModel, TransactionGetRequestModel, TransactionSpecificRequestMoodel
from Server.Repository.TransactionRepository import TransactionRepository

###############################################################################

RepTrans = TransactionRepository()

###############################################################################

async def transaction_new(body:TransactionCreateRequestModel):
    retVal = BaseOutputModel()
    try:
        res = RepTrans.InsertId(body.get_insert_json())
        if res == False:
            retVal.message = "failed inserting transaction"
            retVal.status = 0
            return retVal
        retVal.message = "transaction inserted"
        retVal.result = body.get_insert_json()
        retVal.result["_id"] = str(res)
        retVal.status = 1
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal
    
###############################################################################

async def transaction_getall(body:TransactionGetRequestModel):
    retVal = BaseOutputModel()
    try:
        query = { "$and":[
            {"email":body.email}
        ] }
        data = RepTrans.Get(query)
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

async def transaction_get_specific(body:TransactionSpecificRequestMoodel):
    retVal = BaseOutputModel()
    try:
        query = { "$and": [
            { "_id":ObjectId(body.id) }
        ]}
        data = RepTrans.GetOne(query)
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