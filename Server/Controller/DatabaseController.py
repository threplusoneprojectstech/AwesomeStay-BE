from json import load
from pymongo import MongoClient

def initialize_database(collection_name):
    config = load( open("Server/config.json") )
    connection_string = config["DBUri"]
    client = MongoClient(connection_string)["master"]
    return client[collection_name]