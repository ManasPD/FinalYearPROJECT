import paho.mqtt.client as paho
import hashlib
broker="iot.eclipse.org"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret, ret1= client1.publish("house/bulb1","on")
print ret

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())
#mystring = input('Enter String to hash: ')
# Assumes the default UTF-8

#hash_object = hashlib.md5(mystring.encode())
#print(hash_object.hexdigest())


m = hashlib.md5()
m.update("Nobody inspects")
m.update(" the spammish repetition")
print(m.hexdigest())
print(m.digest_size)
print(m.block_size)