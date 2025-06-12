import pygame


class Settings:
    def __init__(self):
        self.screen = pygame.display.set_mode((500,800), pygame.RESIZABLE)
        pygame.display.set_caption("Rain Drop Animation")
        self.raindrop_image = pygame.image.load("../images/raindrop.png")
        pygame.display.set_icon(self.raindrop_image)
        self.bgcolor = ((40,40,40))
