from fastapi import FastAPI
from pymongo import MongoClient
import redis
from constants import MONGO_URL,DATABASE_NAME,COLLECTION_NAME
from scripts.connect.redis_singleton import RedisWrapper
from scripts.connect.mongo_wrapper import MongoWrapper

app = FastAPI()

mongo_wrapper = MongoWrapper()
collection = mongo_wrapper.collection

# Redis connection
redis_wrapper = RedisWrapper()
redis_client = redis_wrapper.redis_client

@app.get("/readings/")
def get_sensor_readings(start_datetime: str, end_datetime: str):
    # Query MongoDB for readings between start_datetime and end_datetime
    readings = collection.find({
        "timestamp": {
            "$gte": start_datetime,
            "$lte": end_datetime
        }
    })
    result = []
    for reading in readings:
        # Convert ObjectId to string
        reading["_id"] = str(reading["_id"])
        result.append(reading)
    return result

