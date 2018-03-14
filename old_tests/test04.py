# SUMMARY: smoothly blink with LED
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

#PWM SETUP
pwm = GPIO.PWM(ledPin, 50)
pwm.start(75)

#MAIN LOOP

def PwmSine(maxDc, sleepTime):
    for i in range(0,dc):
        os.system('clear')
        pwm.ChangeDutyCycle(i)
        print(str(i*3.3/100)+"V on pin "+str(ledPin))
        time.sleep(sleepTime)
    for i in range(0,dc):
        os.system('clear')
        pwm.ChangeDutyCycle(100-i)
        print(str((100-i)*3.3/100)+"V on pin "+str(ledPin))
        time.sleep(sleepTime)

try:
	while True:
		PwmSine(100, 0.1)

except KeyboardInterrupt:
	pass

# GPIO CLEANUP
pwm.stop()
GPIO.cleanup()

os.system('clear')
print("GPIO closed")
print("\n")
