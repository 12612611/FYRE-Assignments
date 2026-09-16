# Team member names: Anna Zheng, Landon Thoman 
# Purpose of the code: Read in ADC values and convert the values to volts, saving the values to csv 
# Data code was started: 9/16/2026
# Date of last update: 9/16/2026
# Explanation of AI use: AI was used to generate the code 

from machine import ADC, Pin
import time

# -----------------------------
# Settings
# -----------------------------
ADC_PIN = 1
ADC_MAX = 4095
VREF = 3.3
NUM_SAMPLES = 10
SAMPLE_DELAY = 1

# -----------------------------
# Find a new filename
# -----------------------------
file_number = 1

while True:
    filename = "adc_data_{}.csv".format(file_number)

    try:
        # Try to open the file
        with open(filename, "r"):
            pass

        # File exists, try next number
        file_number += 1

    except OSError:
        # File doesn't exist, so this is our new filename
        break

print("Saving data to:", filename)

# -----------------------------
# Set up ADC
# -----------------------------
adc = ADC(Pin(ADC_PIN))

# -----------------------------
# Create new CSV
# -----------------------------
with open(filename, "w") as f:
    f.write("sample,adc_value,voltage_V\n")

# -----------------------------
# Take 10 samples
# -----------------------------
for i in range(NUM_SAMPLES):

    adc_value = adc.read()

    voltage = (adc_value / ADC_MAX) * VREF

    print(
        "Sample {}: ADC = {}, Voltage = {:.4f} V".format(
            i + 1,
            adc_value,
            voltage
        )
    )

    with open(filename, "a") as f:
        f.write(
            "{},{},{:.4f}\n".format(
                i + 1,
                adc_value,
                voltage
            )
        )

    time.sleep(SAMPLE_DELAY)

print("Done!")
print("File saved as:", filename)
