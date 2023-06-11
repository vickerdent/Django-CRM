from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

uri = os.getenv("MONGODB_URI")


def get_database(db_name):
    client = MongoClient(uri)
    
    database = client[db_name]
    return database
