# SUMMARY: blink with LED
# SETUP: connect LED with 50ohms to pin 09(ground) and pin 11 (GPIO17)

import RPi.GPIO as GPIO
import time
import os

#PIN DEFINITIONS
ledPin = 11 # (GPIO17 - Pin 11)

#PIN SETUP
print("Script started")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

#MAIN LOOP

def Blink(iterations, blinkTime):
    for i in range(0, iterations):
        os.system('clear')
        GPIO.output(ledPin, True)
        print("3.3V on pin "+str(ledPin))
        time.sleep(blinkTime)
        os.system('clear')
        GPIO.output(ledPin, False)
        print("0V on pin "+str(ledPin))
        time.sleep(blinkTime)

try:
	while True:
		Blink(50, 3)

except KeyboardInterrupt:
	pass

# GPIO CLEANUP
GPIO.cleanup()

os.system('clear')
print("\n")
print("GPIO closed")
