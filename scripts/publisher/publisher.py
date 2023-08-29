import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
import random
from constants import BROKER,PORT,TIMEOUT

def generate_sensor_data(sensor_type):
    try:
        if sensor_type == "temp":
            return round(random.uniform(15.0,25.0),2)
        if sensor_type == "humidity":
            return round(random.uniform(30,100),1)
    except Exception as e:
        print(e)

def publish_sensor_data(client, sensor_type):
    try:
        sensor_data = {
            "sensor_id": f"{sensor_type}_sensor_{random.randint(1, 2)}",
            "value": generate_sensor_data(sensor_type),
            "timestamp": datetime.now().isoformat()
        }
        client.publish(f"sensors/{sensor_type}",json.dumps(sensor_data))
    except Exception as e:
        print(e)

def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("Connection Established")
    else:
        print("Connection Failed")

def on_publish(client,userdata,mid):
    print("Data Published")

# Initialize

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Connection
client.connect(BROKER,PORT,TIMEOUT)
client.loop_start()

#publish loop
try:
    while True:
        publish_sensor_data(client,"temp")
        publish_sensor_data(client,"humidity")
        time.sleep(5)
except KeyboardInterrupt:
    print("Publisher Stopper")
    client.loop_stop()
    client.disconnect()
