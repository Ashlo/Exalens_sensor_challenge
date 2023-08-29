from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import redis
from constants import MONGO_URL,DATABASE_NAME,COLLECTION_NAME
from connect.redis_singleton import RedisWrapper
from connect.mongo_wrapper import MongoWrapper
import json

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

@app.get("/latest-readings/{sensor_id}")
def get_latest_reading(sensor_id: str):
    try:
        # Get the latest (most recent) sensor reading for the given sensor_id from Redis
        latest_reading = redis_client.lindex(sensor_id, 0)
        
        if latest_reading:
            return JSONResponse(content={"sensor_id": sensor_id, "latest_reading": latest_reading.decode('utf-8')})
        else:
            return JSONResponse(content={"message": "No latest reading found for the sensor"}, status_code=404)

    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)


