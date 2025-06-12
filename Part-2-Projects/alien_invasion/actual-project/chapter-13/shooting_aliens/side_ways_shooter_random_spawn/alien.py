import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, shooter_game):
        super().__init__()
        self.game = shooter_game
        self.settings = self.game.settings
        self.screen = self.settings.screen
        self.image = pygame.image.load("/home/ppv/Documents/ppv-skill-dev/python/codes/github/Python-CrashCourse/Part-2-Projects/alien_invasion/actual-project/chapter-13/images/alien.bmp")
        self.ship_rect  = self.game.ship.image.get_rect()

        self.transformation_ratio = float(self.ship_rect.width/self.image.get_rect().width)

        

        self.image = pygame.transform.scale_by(self.image,self.transformation_ratio)
        self.rect = self.image.get_rect()


        self.rect.x = self.screen.get_rect().width - 2*self.rect.width
        self.rect.y = self.screen.get_rect().height - 2*self.rect.height
