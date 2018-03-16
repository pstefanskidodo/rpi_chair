import pygame
import time

#pygame.display.init()
#pygame.display.set_mode((10,10))
pygame.mixer.init(frequency=22050,size=-16,channels=2)
pygame.init()

testsound = pygame.mixer.Sound("bullet_mono.WAV")
test2 = pygame.mixer.Sound("0975.wav")
ch1 = pygame.mixer.Channel(0)
ch2 = pygame.mixer.Channel(1)
pygame.mixer.set_num_channels(20)

#test2.play()
for i in range(2):
	time.sleep(0.5)
	if i==1:
		ch1.set_volume(0.5617, 0.4419)
		ch2.set_volume(0.4419, 0.5617)
	else:
		ch2.set_volume(0.5617, 0.4419)
		ch1.set_volume(0.4419, 0.5617)
	testsound.play()
	time.sleep(3)