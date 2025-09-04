import os 
from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = os.getenv("MONGODB_URI", "mongodb+srv://root:root@cluster0.cy8op.mongodb.net/")
    client = MongoClient(CONNECTION_STRING)
    return client["pokedex"]

if __name__ == "__main__":
    dbname = get_database()
