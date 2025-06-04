import random
import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((500,800), pygame.RESIZABLE)

pygame.display.set_caption("This is a strobing game")

running = True

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
index = 0

available_colours = [red, green, blue]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Quit successfully")
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            black = (0,0,0) 
            colour = available_colours[index]
            index += 1
            if index > len(available_colours)-1:
                index = index%len(available_colours) 
            screen.fill(colour)

            height, width = screen.get_size()
            exact_center = (int(height/2), int(width/2))
            if colour == red:
                pygame.draw.circle(screen, black, exact_center,20)
            pygame.display.flip()
        
