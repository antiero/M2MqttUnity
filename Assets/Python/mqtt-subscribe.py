import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    try:
        handleRequestMsg(str(message.payload.decode("utf-8")))
    except Exception as inst:
        print("Exception: " + str(inst))

mqttBroker ="mqtt.eclipseprojects.io"
#mqttBroker = "pizero2.local"
client = mqtt.Client("Pi")
client.connect(mqttBroker)
client.loop_start()

client.subscribe("LEDS")
client.on_message=on_message

from led_matrix_handler import LEDMatrix

ledMat = LEDMatrix()
if (not ledMat.process()):
    print("Unable to start the LEDMatrix..")

ledMat.Clear()
def handleRequestMsg(msg):
    print("Msg: " + msg)
    if (msg == "Clear"):
        ledMat.Clear()
    ledChangeRequest = msg.split(',')
    if (len(ledChangeRequest) < 5):
        return
    x = int(ledChangeRequest[0])
    y = int(ledChangeRequest[1])
    r = int(ledChangeRequest[2])
    g = int(ledChangeRequest[3])
    b = int(ledChangeRequest[4])
    ledMat.SetLED(x,y,r,g,b)


while True:
  i=1

ledMat.Clear()
client.loop_stop()
