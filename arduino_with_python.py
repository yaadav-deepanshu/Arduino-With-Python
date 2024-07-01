import serial
import os 
from visual import *

arduino_Serial_Data=serial.Serial("com11","9600")
measuringRod=cylinder(length=6,color=color.yellow,raduis=.5,pos=(-3,0,0))
while(1==1):
    rate(20)
    if (arduino_Serial_Data.in_waiting>0):
        mydata=arduino_Serial_Data.readlines()
        distance=float(arduino_Serial_Data)

