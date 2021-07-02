## Package Import ##
from bson.objectid import ObjectId
## AppCode Import ##
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.AuthRequestModel import *
from Server.Repository.UserRepository import UserRepository
from Server.Utility.Hashing import *
from Server.Utility.JWT import SignJWT

###############################################################################

UserRep = UserRepository()

###############################################################################

async def auth_register(body:ModelRegisterRequest):
    retVal = BaseOutputModel()
    try:
        query = { "$or":[
            {"username":body.username},
            {"email":body.email},
            {"phone":body.phone}
        ] }
        if UserRep.GetOne(query) != None:
            retVal.message = "username / email / phone already taken"
            retVal.status = 0
            return retVal
        else:
            body.password = GenerateHash(body.password)

            if UserRep.Insert(body.getInsertJson()) == False:
                retVal.message = "failed registering user"
                retVal.status = 0
                return retVal

            currUser = UserRep.GetOne(query)
            
            currUser["_id"] = str(currUser["_id"])
            retVal.message = "user registered"
            retVal.result = currUser
            retVal.status = 1
            return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

###############################################################################

async def auth_login(body:ModelLoginRequest):
    retVal = BaseOutputModel()
    try:
        query = { "username":body.username }
        currUser = UserRep.GetOne(query)
        if currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        else:
            if VerifyHash(currUser["password"], body.password):
                currUser["_id"] = str(currUser["_id"])
                currUser["token"] = SignJWT(currUser["_id"])
                retVal.message = "user logged in"
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

###############################################################################

async def auth_user_details(body:ModelUserDetailRequest):
    retVal = BaseOutputModel()
    try:
        query = { "username":body.username }
        currUser = UserRep.GetOne(query)

        if currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        else:
            currUser["_id"] = str(currUser["_id"])
            currUser.pop("password")
            retVal.message = "user found"
            retVal.result = currUser
            retVal.status = 1
            return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal
    
###############################################################################

async def auth_update_user_email(body:ModelUpdateUserEmailRequest):
    retVal = BaseOutputModel()
    try:
        query_validation = { "$and":[
            { "email" : body.updateEmail },
            { "_id" : { "$ne":ObjectId(body.id) } },
            { "username" : { "$ne":body.username } }
        ] }
        query_account = { "$and":[
            { "_id" : ObjectId(body.id) },
            { "username" : body.username }
        ] }

        email_validation = UserRep.GetOne(query_validation)
        currUser = UserRep.GetOne(query_account)
        
        if  email_validation != None:
            retVal.message = "email already taken"
            retVal.status = 0
            return retVal
        if  currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        if VerifyHash(currUser["password"], body.password) == False:
            retVal.message = "wrong password"
            retVal.status = 0
            return retVal
        else:
            set_value = { "$set":
                { "email" : body.updateEmail }
            }
            UserRep.Update(query_account, set_value)
            currUser["_id"] = str(currUser["_id"])
            currUser["email"] = body.updateEmail
            currUser.pop("password")
            currUser.pop("phone")
            retVal.result = currUser
            retVal.message = "email updated"
            retVal.status = 1
            return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

###############################################################################

async def auth_update_user_phone(body:ModelUpdateUserPhoneRequest):
    retVal = BaseOutputModel()
    try:
        query_validation = { "$and":[
            { "phone" : body.updatePhone },
            { "_id" : { "$ne":ObjectId(body.id) } },
            { "username" : { "$ne":body.username } }
        ] }
        query_account = { "$and":[
            { "_id" : ObjectId(body.id) },
            { "username" : body.username }
        ] }

        phone_validation = UserRep.GetOne(query_validation)
        currUser = UserRep.GetOne(query_account)
        
        if  phone_validation != None:
            retVal.message = "phone already taken"
            retVal.status = 0
            return retVal
        if  currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        if VerifyHash(currUser["password"], body.password) == False:
            retVal.message = "wrong password"
            retVal.status = 0
            return retVal
        else:
            set_value = { "$set":
                { "phone" : body.updatePhone }
            }
            UserRep.update_one(query_account, set_value)
            currUser["_id"] = str(currUser["_id"])
            currUser["phone"] = body.updatePhone
            currUser.pop("password")
            currUser.pop("email")
            retVal.result = currUser
            retVal.message = "phone updated"
            retVal.status = 1
            return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

###############################################################################

async def auth_update_user_password(body:ModelUpdateUserPasswordRequest):
    retVal = BaseOutputModel()
    try:
        query_account = { "$and":[
            { "_id" : ObjectId(body.id) },
            { "username" : body.username }
        ] }

        currUser = UserRep.GetOne(query_account)
        
        if  currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        if VerifyHash(currUser["password"], body.password) == False:
            retVal.message = "wrong old password"
            retVal.status = 0
            return retVal
        else:
            body.updatePassword = GenerateHash(body.updatePassword)
            set_value = { "$set":
                { "password" : body.updatePassword }
            }
            UserRep.Update(query_account, set_value)
            currUser["_id"] = str(currUser["_id"])
            currUser["password"] = body.updatePassword
            currUser.pop("email")
            currUser.pop("phone")
            retVal.result = currUser
            retVal.message = "password updated"
            retVal.status = 1
            return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal