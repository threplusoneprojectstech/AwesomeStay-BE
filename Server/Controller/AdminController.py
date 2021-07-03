from Server.Utility.Hashing import *
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Repository.AdminRepository import AdminRepository
from Server.Model.AdminRequestModel import *
from Server.Utility.JWT import SignJWT

###############################################################################

AdminRep = AdminRepository()

###############################################################################

async def admin_insert(body:ModelInsertRequest):
    retVal = BaseOutputModel()
    try:
        query = { "$or":[
                {"username":body.username},
                {"email":body.email},
                {"phone":body.phone}
            ] }
        if AdminRep.GetOne(query) != None:
            retVal.message = "username / email / phone already taken"
            retVal.status = 0
            return retVal
        else:
            body.password = GenerateHash(body.password)

            if AdminRep.Insert(body.getInsertJson()) == False:
                retVal.message = "failed registering admin"
                retVal.status = 0
                return retVal

            currUser = AdminRep.GetOne(query)
            
            currUser["_id"] = str(currUser["_id"])
            retVal.message = "admin registered"
            retVal.result = currUser
            retVal.status = 1
            return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

###############################################################################

async def admin_login(body:ModelLoginRequest):
    retVal = BaseOutputModel()
    try:
        query = { "username":body.username }
        currUser = AdminRep.GetOne(query)
        if currUser == None:
            retVal.message = "admin not found"
            retVal.status = 0
            return retVal
        else:
            if VerifyHash(currUser["password"], body.password):
                currUser["_id"] = str(currUser["_id"])
                currUser["token"] = SignJWT(currUser["_id"])
                retVal.message = "admin logged in"
                retVal.result = currUser
                retVal.status = 1
                return retVal
            else:
                retVal.message = "wrong password"
                retVal.status = 0
                return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal