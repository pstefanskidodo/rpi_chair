# SUMMARY: light a LED
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

GPIO.output(ledPin, True)

#MAIN LOOP

try:
	while True:
		os.system('clear')
		print("3.3V on pin "+str(ledPin))

except KeyboardInterrupt:
	pass

# GPIO CLEANUP
GPIO.cleanup()

os.system('clear')
print("\n")
print("GPIO closed")
