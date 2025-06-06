import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((400,500),pygame.RESIZABLE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            print("pygame method did not work")

        pygame.draw.rect(surface, (255,255,0), pygame.Rect(40,40,60,60))

        pygame.display.flip()

