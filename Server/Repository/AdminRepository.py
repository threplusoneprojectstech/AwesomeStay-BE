from Server.Utility.Database import initialize_database_connection

class AdminRepository():
    def __init__(this):
        this._admin = initialize_database_connection("admin")

    def GetOne(this, Query):
        try:
            return this._admin.find_one(Query)
        except Exception as e:
            print(e)
            return None

    def Get(this, Query=None):
        try:
            if Query:
                return this._admin.find(Query)
            else:
                return this._admin.find()
        except Exception as e:
            print(e)
            return None
    
    def Insert(this, data):
        try:
            this._admin.insert_one(data)
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
                this._admin.update_one(Query, Data)
                return True

        except Exception as e:
            print(e)
            return None