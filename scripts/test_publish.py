import paho.mqtt.client as mqtt

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
print("about to make a connection")
client.connect("localhost",1883,60)
client.loop_start()

client.publish("test/topic","Hello!!")
client.disconnect()
