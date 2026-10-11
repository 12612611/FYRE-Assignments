# Team member names: Anna Zheng, Landon Thoman
# Purpose of the code: The purpose of the code is to simulate a prototype of a landslide wall that is triggered when: 
#                       1) The switch is turned on
#                       2) The photoresistor is covered 
#                       3) Air is blown on the sensor 
#                      When it is triggered, the servo (the wall is attached to the servo) turns to 90 degree and the 
#                      LED continues flashing until the landslide wall isn't triggered. When it's not triggered, the 
#                      servo turns back to 0 degree and the LED stops flashing. 
# Data code was started: 9/23/2026
# Date of last update: 9/28/2026
# Explanation of AI use: AI was used to generate the code and assist with brainstorming. 

from machine import Pin, PWM, ADC
from time import sleep

# -------------------------
# SERVO
# -------------------------
servo = PWM(Pin(5), freq=50)

# -------------------------
# SWITCH
# -------------------------
switch = Pin(6, Pin.IN, Pin.PULL_UP)

# -------------------------
# PHOTORESISTOR
# -------------------------
light_sensor = ADC(Pin(7))
light_sensor.atten(ADC.ATTN_11DB)

# -------------------------
# AIR / BLOW SENSOR
# -------------------------
air_sensor = ADC(Pin(12))

# Blow sensor voltage threshold
air_threshold = 3.0

# -------------------------
# LED
# -------------------------
led = Pin(8, Pin.OUT)

def move_servo(angle):
    min_duty = 1638
    max_duty = 8192

    duty = int(min_duty +
               (angle / 180) * (max_duty - min_duty))

    servo.duty_u16(duty)
  
# -------------------------
# START
# -------------------------
move_servo(0)
led.off()

# -------------------------
# MAIN LOOP
# -------------------------
while True:

    # -------------------------
    # BUTTON
    # -------------------------
    switch_pressed = (switch.value() == 0)

    # -------------------------
    # PHOTORESISTOR
    # -------------------------
    light_value = light_sensor.read()

    # Light covered → higher reading
    light_covered = light_value > 1500

    # -------------------------
    # AIR / BLOW SENSOR
    # -------------------------
    air_value = air_sensor.read_u16()

    # Convert ADC reading to voltage
    air_voltage = (air_value / 65535) * 3.3

    # Above 3.0 V → blown on
    air_detected = air_voltage > air_threshold

    # -------------------------
    # TRIGGER
    # -------------------------
    # Button OR light covered OR blown on
    if switch_pressed or light_covered or air_detected:

        # Move servo to 90°
        move_servo(90)

        # Flash LED
        led.on()
        sleep(0.25)

        led.off()
        sleep(0.25)

    else:

        # Move servo back to 0°
        move_servo(0)

        # LED OFF
        led.off()

        sleep(0.05)
