import paho.mqtt.client as mqtt
import json
from constants import BROKER,PORT,TIMEOUT,MONGO_URL,DATABASE_NAME,COLLECTION_NAME
from pymongo import MongoClient

# Connect to the MongoDB server
mongo_client = MongoClient(MONGO_URL)
db = mongo_client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def on_connect(client,userdata,flags,rc):
    try:
        print("Connected")
        client.subscribe("sensors/temp")
        client.subscribe("sensors/humidity")
    except Exception as e:
        print(e)

def on_message(client,userdata,msg):
    try:
        print(msg.topic,msg.payload.decode('utf-8'))
        data = json.loads(msg.payload)

        #TODO Mongo_json final structure
        mongo_json = {
        "topic": msg.topic,
        "message": msg.payload.decode()
        }

        collection.insert_one(mongo_json)
        print(f"Recieved data from {data['sensor_id']:}:{data['value']} at {data['timestamp']}")
    except Exception as e:
        print(e)

# initailize

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER,PORT,TIMEOUT)
client.loop_forever()
