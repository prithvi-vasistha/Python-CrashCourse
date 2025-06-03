import pygame
import sys

pygame.init()
pygame.display.set_mode((500,500))
pygame.display.set_caption("This is a non-resizable window")


while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
