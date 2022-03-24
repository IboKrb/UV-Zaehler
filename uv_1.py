import board
import adafruit_veml6070
import time
import serial

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
        
        
        
        
