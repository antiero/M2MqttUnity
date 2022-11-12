import paho.mqtt.client as mqtt 
from random import randrange, uniform, randint
import time

mqttBroker ="mqtt.eclipseprojects.io" 
#mqttBroker = "pizero2.local"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

while True:
    X = randint(1, 32)
    Y = randint(1, 32)
    R = randint(1, 255)
    G = randint(1, 255)
    B = randint(1, 255)
    xyrgbstring = "%d,%d,%d,%d,%d" % (X,Y,R,G,B)
    client.publish("LEDS", xyrgbstring)
    #print("Just published " + str(xyrgbstring) + " to topic TEMPERATURE")
    #time.sleep(1.0/10.0)
