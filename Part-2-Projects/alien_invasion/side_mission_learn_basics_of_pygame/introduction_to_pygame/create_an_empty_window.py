import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400,1200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
