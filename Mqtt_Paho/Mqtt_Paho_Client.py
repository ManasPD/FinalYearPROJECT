import paho.mqtt.client as mqtt   #importing the paho mqtt client library
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address = "iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1")        #creating a new client instance
client.on_message=on_message
print("connecting to broker")
client.connect(broker_address)      #connect to broker

print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")   #subscribing to a topic
print('Publishing message to topic','house/bulbs/bulb1')
client.loop_start()
client.publish("house/bulbs/bulb1","OFF")   #publishing to a topic
time.sleep(4) # wait
client.loop_stop()