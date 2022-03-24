import time
import board
import adafruit_veml6070
import serial
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED

gelb=LED(16)
grün=LED(13)
rot=LED(6)

rot2=LED(24)
grün2=LED(22)
gelb2=LED(17)

ser = serial.Serial ("/dev/ttyS0", 9600)

with board.I2C() as i2c:
    uv = adafruit_veml6070.VEML6070(i2c)

    while True:
        uv_raw = uv.uv_raw
        risk_level = uv.get_index(uv_raw)
        uv_zahl=uv_raw
        print("Reading: {0} | Risk Level: {1}".format(uv_raw, risk_level))
        ser.write(str.encode(str(uv_raw)))
        time.sleep(1)
        received_data = ser.read()              
        sleep(0.03)
        data_left = ser.inWaiting()             
        received_data += ser.read(data_left)                  
        uv2_zahl=int(received_data)
        print("UV:"uv2_zahl)
        
         if uv_zahl >= 500 :
            grün.on()
        if uv_zahl >= 900 :
            gelb.on()
        if uv_zahl >= 1200 :
            rot.on()
        if uv_zahl < 500:
            grün.off()
        if uv_zahl < 900:
            gelb.off()
        if uv_zahl < 1200:
            rot.off()
            
        if uv2_zahl >= 500 :
            grün2.on()
            
        if uv2_zahl >= 900 :
            gelb2.on()
            
        if uv2_zahl >= 1200 :
            rot2.on()
            
        if uv2_zahl < 500:
            grün2.off()
            
        if uv2_zahl < 900:
            gelb2.off()
            
        if uv2_zahl < 1200:
            rot2.off()
        
        
        
        
