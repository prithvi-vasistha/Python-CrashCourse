import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500,800), pygame.RESIZABLE)
pygame.display.set_caption("Example 2")
font = pygame.font.Font(None, 36)
color = (0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            key = str(event.key)
            text = font.render(key, True, (255,255,255))
            screen.blit(text, (10,10))
            print(event.key)

            

