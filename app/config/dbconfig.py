import os 
from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = os.getenv("MONGODB_URI")
    client = MongoClient(CONNECTION_STRING)
    return client["pokemon"]

if __name__ == "__main__":
    dbname = get_database()
