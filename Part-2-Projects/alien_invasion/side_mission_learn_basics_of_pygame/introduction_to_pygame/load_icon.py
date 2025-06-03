import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
pygame.display.set_caption("this is a sample window")
Image = pygame.image.load("apple_158989157.jpg")


pygame.display.set_icon(Image)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
