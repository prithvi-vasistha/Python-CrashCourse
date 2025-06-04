import random
import time
import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((500,800), pygame.RESIZABLE)

pygame.display.set_caption("This is a strobing game")

running = True

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
index = 0

available_colours = [red, green, blue]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Quit successfully")
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            colour = available_colours[index]
            index += 1
            if index > 2:
                index = 0
            screen.fill(colour)
            pygame.display.flip()
        else:
            pass
