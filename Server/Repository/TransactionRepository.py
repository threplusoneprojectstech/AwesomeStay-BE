from Server.Utility.Database import initialize_database_connection

class TransactionRepository():
    def __init__(this):
        this._transaction = initialize_database_connection("transaction")

    def GetOne(this, Query):
        try:
            return this._transaction.find_one(Query)
        except Exception as e:
            print(e)
            return None

    def Get(this, Query=None):
        try:
            if Query:
                return this._transaction.find(Query)
            else:
                return this._transaction.find()
        except Exception as e:
            print(e)
            return None
    
    def Insert(this, data):
        try:
            this._transaction.insert_one(data)
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
                this._transaction.update_one(Query, Data)
                return True

        except Exception as e:
            print(e)
            return None