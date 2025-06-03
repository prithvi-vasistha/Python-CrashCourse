import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))

x, y = screen.get_size()
pygame.display.quit()

print(x,y)
