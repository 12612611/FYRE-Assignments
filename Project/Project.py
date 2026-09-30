# Team member names: Anna Zheng, Landon Thoman
# Purpose of the code: Prototype of landslide wall
# Data code was started: 9/23/2026
# Date of last update: 9/30/2026
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
air_sensor.atten(ADC.ATTN_11DB)

# Blow sensor resistance threshold
air_threshold = 50

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
    air_value = air_sensor.read_uv()
    air_value = air_value / 1000

    rknown = 330

    # Calculate sensor resistance
    air_resistance = rknown * (
        air_value / (3300 - air_value)
    )

    # Below 85 ohms → blown on
    air_detected = air_resistance < air_threshold

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
