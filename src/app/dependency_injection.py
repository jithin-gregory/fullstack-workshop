from config import MONGO_CONFIG
from database.MongoDBClient import MongoDBClient


def mongo_client():
    client = MongoDBClient(uri=MONGO_CONFIG.MONGO_URI, database_name=MONGO_CONFIG.MONGO_DATABASE)
    return client.get_instance()
