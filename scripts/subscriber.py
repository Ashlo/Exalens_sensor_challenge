import paho.mqtt.client as mqtt
import json


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

        #TODO MONGO DB LOGICS Insertion

        print(f"Recieved data from {data['sensor_id']:}:{data['value']} at {data['timestamp']}")
    except Exception as e:
        print(e)

# initailize

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost",1883,60)
client.loop_forever()
