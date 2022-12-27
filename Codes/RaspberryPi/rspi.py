# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
import os
import os.path

import paho.mqtt.client as mqtt
#motors###########################################################
import RPi.GPIO as GPIO          
from time import sleep
#sidewards
in1 = 24
in2 = 23
en = 25
temp1=1
in3 = 15
in4 = 14
enB = 18

#fronts
in5 = 20
in6 = 16
enC = 21

in7 = 1
in8 = 7
enD = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
####################
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
###################
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(enC,GPIO.OUT)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
###################
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(enD,GPIO.OUT)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)
###################
p=GPIO.PWM(en,1000)
q=GPIO.PWM(enB,1000)
r=GPIO.PWM(enC,1000)
s=GPIO.PWM(enD,1000)
p.start(100)
q.start(100)
r.start(100)
s.start(100)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("q- upper rest t-forward rest e-exit")
print("\n")    
#upper motion
def UpLift():
    GPIO.output(in5,GPIO.HIGH)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.HIGH)
    GPIO.output(in8,GPIO.LOW)
def DownLift():
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.HIGH)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.HIGH)
def Reset1():
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.LOW)
#forward motion
def Forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
def Backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
def Left():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
def Right():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
def Reset2():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

##################################################################
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("xquest/test")
    print("Subscribed to xquest/test")
    
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(str(msg.payload))
    text = str(msg.payload)[2:-1]
    
    print(text)

    if text == "Camera":
        print("Turning on camera stream... ")
        # Camera stream
        os.system('libcamera-vid -t 0 --inline --framerate 60 --listen -o tcp://0.0.0.0:8080')

    if text == "Up":
        UpLift()
    if text == "Down":
        DownLift()
    if text == "Left":
        Left()
    if text == "Right":
        Right()
    if text == "Forward":
        Forward()
    if text == "Backward":
        Backward()
    if text == "reset1":
        Reset1()
    if text == "reset2":
        Reset2()
        # Do something else
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("broker.hivemq.com")
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()