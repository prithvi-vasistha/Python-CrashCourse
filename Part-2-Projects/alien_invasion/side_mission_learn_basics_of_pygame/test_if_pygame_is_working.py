import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Test to check if pygame is working")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
