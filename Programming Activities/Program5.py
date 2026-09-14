from machine import Pin
import time

button = Pin(18, Pin.IN)
led = Pin(8, Pin.OUT)

while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
