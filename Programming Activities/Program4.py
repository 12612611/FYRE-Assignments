# Blinking program

# Incorporate our module 
import machine #module with all the microcontroller stuff 
import time #module with time methods

# Make our led object 
# Green led is GPIO Pin 0
led = machine.Pin(0, machine.Pin.OUT)

# Infinite loop 
while True: 
  led.value(1) #turn on the led
  time.sleep(0.25) #25 second delay
  led.value(0) #turn off the led
  time.sleep(0.25) #25 second delay again 
  