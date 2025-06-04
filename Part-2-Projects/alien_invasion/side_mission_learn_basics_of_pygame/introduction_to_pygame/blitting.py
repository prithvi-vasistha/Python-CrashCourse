""" for a surface to be displayed, it needs to be blitted;
    blitting can be thought of as copying pixels from one surface to another
    surface.blit() method is used to achieve the same """

import pygame
import time
import sys

pygame.init()

surface = pygame.display.set_mode((400,600),pygame.RESIZABLE)

image1 = pygame.image.load("/home/ppv/Documents/ppv-skill-dev/python/codes/github/Python-CrashCourse/Part-2-Projects/alien_invasion/side_mission_learn_basics_of_pygame/introduction_to_pygame/apple_158989157.jpg")

image2 = pygame.image.load("/home/ppv/Documents/ppv-skill-dev/python/codes/github/Python-CrashCourse/Part-2-Projects/alien_invasion/side_mission_learn_basics_of_pygame/introduction_to_pygame/apple_158989157.jpg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        surface.blit(image1, (0,0))
        pygame.display.flip()
        time.sleep(5)
        surface.blit(image1, (300,500))
        pygame.display.flip()
