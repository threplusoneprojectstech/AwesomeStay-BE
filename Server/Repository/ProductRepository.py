from Server.Utility.Database import initialize_database_connection

class ProductRepository():
    def __init__(this):
        this._product = initialize_database_connection("product")

    def GetOne(this, Query):
        try:
            return this._product.find_one(Query)
        except Exception as e:
            print(e)
            return None

    def Get(this, Query=None):
        try:
            if Query:
                return this._product.find(Query)
            else:
                return list(this._product.find().sort([
                    ("rating",1),
                    ("userRateCount",1)
                ]))
        except Exception as e:
            print(e)
            return None
    
    def GetPages(this, pageNum=1, pageSize=10, Query=None):
        try:
            skips = pageSize * (pageNum - 1)
            if Query:
                cur = this._product.find(Query).skip(skips).limit(pageSize)
                return list(cur)
            else:
                cur = this._product.find().sort([
                    ("rating",1),
                    ("userRateCount",1)
                ]).skip(skips).limit(pageSize)
                return list(cur)
        except Exception as e:
            print(e)
            return None

    def GetCount(this):
        try:
            return this._product.count()
        except Exception as e:
            print(e)
            return None

    def Insert(this, data):
        try:
            print("try ins")
            this._product.insert_one(data)
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
                this._product.update_one(Query, Data)
                return True

        except Exception as e:
            print(e)
            return None