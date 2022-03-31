import time
import board
import adafruit_veml6070
import serial
from gpiozero import LED

class uv_sensor():
    def __init__(self, uv):
        self.uv = uv
        self.uv_raw = self.uv.uv_raw
        self.risk_level = self.uv.get_index(self.uv_raw)
        self.gelb=LED(16)
        self.grün=LED(13)
        self.rot=LED(6)

        self.rot2=LED(24)
        self.grün2=LED(17)
        self.gelb2=LED(22)

    def report(self):
        print("Reading: {0} | Risk Level: {1}".format(self.uv_zahl, self.risk_level))
        print ("UV-Wert vom zweiten Sensor:",self.uv2_zahl)                   

    def read(self):
        self.uv_raw = self.uv.uv_raw
        self.uv_zahl=self.uv_raw
        self.risk_level = self.uv.get_index(self.uv_zahl)
        
    def ser_read(self):
        self.received_data = ser.read()
        self.data_left = ser.inWaiting()             
        self.received_data += ser.read(self.data_left)
        self.uv2_zahl=int(self.received_data)

    def Led_on(self):
        if self.uv_zahl >= 0 :
            self.grün.on()
        if self.uv_zahl >= 600 :
            self.gelb.on()
        if self.uv_zahl >= 1000 :
            self.rot.on()
        if self.uv_zahl < 600:
            self.gelb.off()
        if self.uv_zahl < 1000:
            self.rot.off()
            
        if self.uv2_zahl >= 0 :
            self.grün2.on()
            
        if self.uv2_zahl >= 600 :
            self.gelb2.on()
            
        if self.uv2_zahl >= 1000 :
            self.rot2.on()
    
            
        if self.uv2_zahl < 600:
            self.gelb2.off()
            
        if self.uv2_zahl < 1000:
            self.rot2.off()

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate

with board.I2C() as i2c:
    uv = adafruit_veml6070.VEML6070(i2c)
    sensor = uv_sensor(uv)

    while True:
        

        sensor.read()
        sensor.ser_read()
        sensor.report()
        sensor.Led_on()
        time.sleep(1)

        
        
        
