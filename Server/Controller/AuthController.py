from bson.objectid import ObjectId
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.AuthRequestModel import *

async def auth_register(USER_COLLECTION, body:ModelRegisterRequest):
    retVal = BaseOutputModel()
    try:
        query = { "$or":[
            {"username":body.username},
            {"email":body.email},
            {"phone":body.phone}
        ] }
        if USER_COLLECTION.find_one(query) != None:
            retVal.message = "username / email / phone already taken"
            retVal.status = 0
            return retVal
        else:
            USER_COLLECTION.insert_one(body.getInsertJson())
            currUser = USER_COLLECTION.find_one(query)
            currUser["_id"] = str(currUser["_id"])
            retVal.message = "user registered"
            retVal.result = currUser
            retVal.status = 1
            return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

async def auth_login(USER_COLLECTION, body:ModelLoginRequest):
    retVal = BaseOutputModel()
    try:
        query = { "username":body.username }
        currUser = USER_COLLECTION.find_one(query)
        if currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        else:
            if body.password == currUser["password"]:
                currUser["_id"] = str(currUser["_id"])
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

async def auth_user_details(USER_COLLECTION, body:ModelUserDetailRequest):
    retVal = BaseOutputModel()
    try:
        query = { "username":body.username }
        currUser = USER_COLLECTION.find_one(query)
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
    
async def auth_update_user_email(USER_COLLECTION, body:ModelUpdateUserEmailRequest):
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
        email_validation = USER_COLLECTION.find_one(query_validation)
        currUser = USER_COLLECTION.find_one(query_account)
        

        if  email_validation != None:
            retVal.message = "email already taken"
            retVal.status = 0
            return retVal
        if  currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        if body.password != currUser["password"]:
            retVal.message = "wrong password"
            retVal.status = 0
            return retVal
        else:
            set_value = { "$set":
                { "email" : body.updateEmail }
            }
            USER_COLLECTION.update_one(query_account, set_value)
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

async def auth_update_user_phone(USER_COLLECTION, body:ModelUpdateUserPhoneRequest):
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
        phone_validation = USER_COLLECTION.find_one(query_validation)
        currUser = USER_COLLECTION.find_one(query_account)
        

        if  phone_validation != None:
            retVal.message = "phone already taken"
            retVal.status = 0
            return retVal
        if  currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        if body.password != currUser["password"]:
            retVal.message = "wrong password"
            retVal.status = 0
            return retVal
        else:
            set_value = { "$set":
                { "phone" : body.updatePhone }
            }
            USER_COLLECTION.update_one(query_account, set_value)
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

async def auth_update_user_password(USER_COLLECTION, body:ModelUpdateUserPasswordRequest):
    retVal = BaseOutputModel()
    try:
        query_account = { "$and":[
            { "_id" : ObjectId(body.id) },
            { "username" : body.username }
        ] }
        currUser = USER_COLLECTION.find_one(query_account)
        
        if  currUser == None:
            retVal.message = "user not found"
            retVal.status = 0
            return retVal
        if body.password != currUser["password"]:
            retVal.message = "wrong old password"
            retVal.status = 0
            return retVal
        else:
            set_value = { "$set":
                { "password" : body.updatePassword }
            }
            USER_COLLECTION.update_one(query_account, set_value)
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