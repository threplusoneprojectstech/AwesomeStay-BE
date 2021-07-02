import os
from json import load
from pymongo import MongoClient

def initialize_database_connection(collection_name):
    connection_string = ""
    try:
        config = load( open("Server/config.json") )
        connection_string = config["DBUri"]
    except:
        print("> loading config from os variable")
        try:
            connection_string = os.environ["DBUri"]
        except:
            print("> failed to load from environment variable")
    client = MongoClient(connection_string)["master"]
    return client[collection_name]