# Team member names: Anna Zheng, Landon Thoman 
# Purpose of the code: Prototype of landslide wall 
# Data code was started: 9/23/2026
# Date of last update: 9/23/2026
# Explanation of AI use: AI was used to generate the code 

## plan of action: 
## make servo push wall by push button switch ok 
## or by photoresistor light sensor being blocked ok 
## trigger by rain sensor (replace w our own sensor) dropping to certain voltage 
## when servo moves to 90, led flashes ok 

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
# LED
# -------------------------
led = Pin(8, Pin.OUT)


def move_servo(angle):
    min_duty = 1638
    max_duty = 8192

    duty = int(min_duty +
               (angle / 180) * (max_duty - min_duty))

    servo.duty_u16(duty)


# Start at 0 degrees
move_servo(0)
led.off()


while True:

    switch_pressed = (switch.value() == 0)

    light_value = light_sensor.read()

    # Light covered → higher reading
    light_covered = light_value > 1500

    # Switch OR light covered
    if switch_pressed or light_covered:
        # Move servo to 90°
        move_servo(90)

        # Turn LED ON
        led.on()

    else:
        # Move servo back to 0°
        move_servo(0)

        # Turn LED OFF
        led.off()

    sleep(0.05)
