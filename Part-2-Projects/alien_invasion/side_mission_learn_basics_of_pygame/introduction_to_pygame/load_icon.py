import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
pygame.display.set_caption("this is a sample window")

try:
    Image = pygame.image.load("apple_158989157.jpg")
    pygame.display.set_icon(Image)
    print("image loaded successfully")

except Exception as e:
    print("Image did not load because of this exception")
    print(e)
    pass

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
