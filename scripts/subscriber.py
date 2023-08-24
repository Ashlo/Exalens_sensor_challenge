import paho.mqtt.client as mqtt
import json
from constants import BROKER,PORT,TIMEOUT,MONGO_URL,DATABASE_NAME,COLLECTION_NAME
from bson.objectid import ObjectId
from scripts.connect.redis_singleton import RedisWrapper
from scripts.connect.mongo_wrapper import MongoWrapper

# Connect to the local Redis instance

redis_wrapper = RedisWrapper()
redis_client = redis_wrapper.redis_client
#TODO Redis implementation

# Connect to the MongoDB server
mongo_wrapper = MongoWrapper()
collection = mongo_wrapper.collection


def jsonify_mongo_data(data):
    """Converts data containing MongoDB's ObjectId to JSON-serializable format"""
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, ObjectId):
                data[k] = str(v)
            else:
                jsonify_mongo_data(v)
    elif isinstance(data, list):
        for i, v in enumerate(data):
            if isinstance(v, ObjectId):
                data[i] = str(v)
            else:
                jsonify_mongo_data(v)
    return data


def on_connect(client,userdata,flags,rc):
    try:
        print("Connected")
        client.subscribe("sensors/temp")
        client.subscribe("sensors/humidity")
    except Exception as e:
        print(e)

def on_message(client,userdata,msg):
    try:
        payload_dict = json.loads(msg.payload.decode('utf-8'))

        mongo_json = {
            "topic": msg.topic,
            **payload_dict
            }

        collection.insert_one(mongo_json)

        # Store the latest 10 readings for each sensor in Redis
        # Redis Lists will be used here
        # LPUSH adds a value to the front of the list, LTRIM ensures we only keep the latest 10
        serializable_data = jsonify_mongo_data(mongo_json)
        redis_key = serializable_data['sensor_id']
        print(redis_key)
        redis_client.lpush(redis_key, json.dumps(serializable_data))
        redis_client.ltrim(redis_key, 0, 9)
    except Exception as e:
        print(e)

# initailize

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER,PORT,TIMEOUT)
client.loop_forever()