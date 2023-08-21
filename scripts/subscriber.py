import paho.mqtt.client as mqtt
import json
from constants import BROKER,PORT,TIMEOUT,MONGO_URL,DATABASE_NAME,COLLECTION_NAME
from pymongo import MongoClient
from datetime import datetime

#TODO Redis implementation

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
        payload_dict = json.loads(msg.payload.decode('utf-8'))

        mongo_json = {
            "topic": msg.topic,
            **payload_dict
            }

        collection.insert_one(mongo_json)
    except Exception as e:
        print(e)

# initailize

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER,PORT,TIMEOUT)
client.loop_forever()