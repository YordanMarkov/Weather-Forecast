#!/usr/bin/env python
import time
import Adafruit_GPIO.SPI as SPI
from adafruit_bme280 import *
import board
import busio
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = Adafruit_BME280_I2C(i2c, address=0x76)
    temp = int(sensor.temperature)
    hum = int(sensor.humidity)
    pre = int(sensor.pressure)
    
    return render_template('sait.html', temp=temp, hum=hum, pre=pre)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

