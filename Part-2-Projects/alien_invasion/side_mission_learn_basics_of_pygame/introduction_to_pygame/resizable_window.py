import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)

pygame.display.set_caption("This is a resizable window")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
