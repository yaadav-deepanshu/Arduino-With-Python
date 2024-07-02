import serial

from visual import *

arduino_Serial_Data=serial.Serial("com11","9600")
measuringRod=cylinder(length=6,color=color.yellow,raduis=.5,pos=(-3,0,0))
while(1==1):
    rate(20)
    if (arduino_Serial_Data.in_waiting>0):
        mydata=arduino_Serial_Data.readlines()
        distance=float(arduino_Serial_Data)


for i in range(100):
    if i%2==0:
        print("even")

    else: 
        print("odd")              

