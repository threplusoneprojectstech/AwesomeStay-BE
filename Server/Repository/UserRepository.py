from os import truncate
from pymongo.message import query
from Server.Utility.Database import initialize_database_connection

class UserRepository():
    def __init__(this):
        this._user = initialize_database_connection("user")

    def GetOne(this, Query):
        try:
            return this._user.find_one(Query)
        except Exception as e:
            print(e)
            return None

    def Get(this, Query=None):
        try:
            if query:
                return this._user.find(Query)
            else:
                return this._user.find()
        except Exception as e:
            print(e)
            return None
    
    def Insert(this, data):
        try:
            this._user.insert_one(data)
            return True
        except Exception as e:
            print(e)
            return False

    def Update(this, Query=None, Data=None):
        try:
            if Data==None or Query == None:
                print("Exception: [Update] Data or query cannot be null")
                return None
            else:
                this._user.update_one(Query, Data)
                return True

        except Exception as e:
            print(e)
            return None