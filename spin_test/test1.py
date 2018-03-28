# SKRYPT KOMPATYBILNY Z PYTHONEM 3.x !!!
#
# pin 12 jako wyjście PWM, zmiana kierunku:
# pin 16 do obrotu w prawo
# pin 18 do obrotu w lewo 
# 								tabela prawdy :
#
# 							 pin  | 16  | 18 |    12
# 					 obrót w lewo |  0  | 1	 |  0-100%
# 					obrót w prawo |  1  | 0  |  0-100%
# 						  hamulec |  0  | 0  |  not used
# stan zakazany/silnik zawieszony |  1  | 1  |  not used
"""
Opis skryptu:
Po włączeniu na pinie 12 ustawiany jest sygnał PWM, którego stopień wypełnienia zmienia
się od 0% do 100%. Kierunek obrotu silnika powinien być sterowany dwoma pinani: 16 oraz 18.
Po ustawieniu pinu 16 u stan wysoki (pin 18 musi być ustawiony w stanie niskim)
silnik powinien obracać się w prawo. Po ustawieniu pinu 18 u stan wysoki 
(pin 16 musi być ustawiony w stanie niskim) silnik powinien obracać się w lewo.
Gdy piny 16 i 18 ustawione są w stanie niskim silnik powinien się zatrzymać. 
Stan, w którym piny 16 i 18 ustawione są w stanie wysokim, jest zakazany.

Seksencja ruchu:
1. Obrót silnika w prawo od prędkości zerowej do maksymalnej
2. Obrót silnika w prawo od prędkości maksymalnej do zerowej
3. Zatrzymanie silnika na 5s
4. Obrót silnika w lefo od prędkości zerowej do maksymalnej
5. Obrót silnika od prędkości maksymalnej do zerowej
6. Zatrzymanie silnika

Uwaga: Aby zaptrzymać program w trakcie jego działania należy wcisnąć 
kombinacje klawiszy Ctrl+C !!!
"""
import RPi.GPIO	as GPIO
import time
import os

# Sleep time between speed changing
sleep_time = 0.2

#PWM frequency setup
freq = 5000

#Pin definition
PWM_pin = 12
turn_right = 16
turn_left = 18

#GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM_pin, GPIO.OUT)
GPIO.setup(turn_right, GPIO.OUT)
GPIO.setup(turn_left, GPIO.OUT)

#PWM setup
pwm = GPIO.PWM(PWM_pin, freq)
pwm.start(0)

#MAIN LOOP
#increasing speed from 0% to 100% and decreasing inversely every 0.5s
def PwmTest (maxDutyCycle, sleepTime, turnDirection):
	if turnDirection == 'left':
		GPIO.output(turn_right, False)
		GPIO.output(turn_left, True)
	elif turnDirection == 'right':
		GPIO.output(turn_left, False)
		GPIO.output(turn_right, True)
	for i in range(0,maxDutyCycle):
		os.system('clear')
		pwm.ChangeDutyCycle(i)
		print(str(i*3.3/100) + 'V on pin ' + str(PWM_pin))
		print('Speed: ' + str(i))
		print('Drive is turning ' + turnDirection)
		time.sleep(sleepTime)
	for i in range(maxDutyCycle,0,-1):
		os.system('clear')
		pwm.ChangeDutyCycle(i)
		print(str(i*3.3/100) + 'V on pin ' + str(PWM_pin))
		print('Speed: ' + str(i))
		print('Drive is turning ' + turnDirection)
		time.sleep(sleepTime)

try:
	GPIO.output(turn_left, False)
	GPIO.output(turn_right, False)
	time.sleep(0.1)
	PwmTest(100,sleep_time,'left')
	os.system('clear')
	print('Drive stops for 5 sec')
	GPIO.output(turn_left, False)
	GPIO.output(turn_right, False)
	time.sleep(5)
	PwmTest(100,sleep_time,'right')
	GPIO.output(turn_left, False)
	GPIO.output(turn_right, False)
	time.sleep(0.2)
except KeyboardInterrupt:
	pass

#GPIO Cleanup
pwm.ChangeDutyCycle(0)
GPIO.output(turn_left, False)
GPIO.output(turn_right, False)
pwm.stop()
GPIO.cleanup()

os.system('clear')
print('GPIO closed, program closing...')