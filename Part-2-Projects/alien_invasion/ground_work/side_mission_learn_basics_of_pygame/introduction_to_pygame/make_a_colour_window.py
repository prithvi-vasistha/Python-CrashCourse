import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,800),pygame.RESIZABLE)
pygame.display.set_caption("this is a coloured window")

colour = [165, 42, 42]

screen.fill(colour)
pygame.display.flip()

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


