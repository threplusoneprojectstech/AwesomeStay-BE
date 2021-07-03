from Server.Utility.Database import initialize_database_connection

class ChatRepository():
    def __init__(this):
        this._chat = initialize_database_connection("chat")

    def GetOne(this, Query):
        try:
            return this._chat.find_one(Query)
        except Exception as e:
            print(e)
            return None

    def Get(this, Query=None):
        try:
            if Query:
                return this._chat.find(Query)
            else:
                return this._chat.find()
        except Exception as e:
            print(e)
            return None
    
    def Insert(this, data):
        try:
            this._chat.insert_one(data)
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
                this._chat.update_one(Query, Data)
                return True

        except Exception as e:
            print(e)
            return None