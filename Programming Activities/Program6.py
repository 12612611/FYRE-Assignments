# Team member names: Anna Zheng, Landon Thoman
# Purpose of the code: Control a servo arm using a switch. If pressed, it should be oriented at 180; if not pressed, it should be oriented at 0.
# Date code was started: 9/16/2026
# Date of last update: 9/16/2026
# Explanation of AI use: AI was used to generate the code. 

from machine import Pin, PWM
from time import sleep

# -------------------------
# Pin configuration
# -------------------------
SWITCH_PIN = 17
SERVO_PIN = 18

switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)

servo = PWM(Pin(SERVO_PIN))
servo.freq(50)


# -------------------------
# Servo positions
# -------------------------
# These values may need calibration
# for your particular servo.

ZERO_DEG = 1000      # 0° = -X axis = LEFT
ONE_EIGHTY_DEG = 2000  # 180° = +X axis = RIGHT


def servo_us(us):
    # 50 Hz = 20,000 microsecond period
    duty = int(us * 65535 / 20000)
    servo.duty_u16(duty)


# -------------------------
# START AT 0°
# -------------------------
servo_us(ZERO_DEG)

# Give the servo time to reach 0°
sleep(2)


# -------------------------
# MAIN LOOP
# -------------------------
while True:

    if switch.value() == 0:
        # SWITCH PRESSED
        # Rotate 180° CCW → +X axis
        servo_us(ONE_EIGHTY_DEG)

    else:
        # SWITCH RELEASED
        # Return to 0° → -X axis
        servo_us(ZERO_DEG)

    sleep(0.05)
