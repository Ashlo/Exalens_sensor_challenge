import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print("Connected")
    client.subscribe("test/topic")

def on_message(client,userdata,msg):
    print(msg.payload)

# initailize

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

if client.connect("localhost",1883,60) == 0:
    print("Connection established")
client.loop_forever()
