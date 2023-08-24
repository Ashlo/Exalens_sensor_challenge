from pymongo import MongoClient
from constants import MONGO_URL, DATABASE_NAME, COLLECTION_NAME 

class MongoWrapper:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating a new MongoDB connection")
            cls._instance = super(MongoWrapper, cls).__new__(cls)
            cls._instance.mongo_client = MongoClient(MONGO_URL)
            cls._instance.db = cls._instance.mongo_client[DATABASE_NAME]
            cls._instance.collection = cls._instance.db[COLLECTION_NAME]
        return cls._instance

    def insert_one(self, document):
        self.collection.insert_one(document)

    def find(self, query):
        return self.collection.find(query)
