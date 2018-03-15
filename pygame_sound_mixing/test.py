import pygame
import time

#pygame.display.init()
#pygame.display.set_mode((10,10))
pygame.mixer.init(frequency=22050,size=-16,channels=4)
pygame.init()

testsound = pygame.mixer.Sound("bullet.wav")
test2 = pygame.mixer.Sound("0975.wav")
#ch1 = pygame.mixer.find_channel()
#ch2 = pygame.mixer.find_channel()
pygame.mixer.set_num_channels(20)

test2.play()
for i in range(20):
	time.sleep(0.5)
	testsound.play()
	time.sleep(10)