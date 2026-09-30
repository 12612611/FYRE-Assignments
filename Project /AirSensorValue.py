# Team member names: Anna Zheng, Landon Thoman
# Purpose of the code: Measures resistance value of sensor 
# Data code was started: 9/28/2026
# Date of last update: 9/30/2026
# Explanation of AI use: AI was used to generate the code and assist with brainstorming.

from machine import Pin, ADC
from time import sleep

air_sensor = ADC(Pin(12))
air_sensor.atten(ADC.ATTN_11DB)

while True:
    air_value = air_sensor.read_uv() 
    air_value = air_value / 1000
    print(air_value)
    rknown=330
    r = rknown*(air_value/(3300-air_value))
    print(r, "ohm")
    sleep(0.2)
