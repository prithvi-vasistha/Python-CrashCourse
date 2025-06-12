import pygame
from pygame.sprite import Sprite
import random


class Raindrop(Sprite):
    def __init__(self, program):
        super().__init__()
        self.settings = program.settings
        self.image = self.settings.raindrop_image
        self.screen = self.settings.screen
        self._resize_image()
        self._position_image()
    


    def _resize_image(self):
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.target_height = int(0.05*self.screen_rect.height)
        scaling_factor = self.target_height/self.rect.height
        self.target_width = int(self.rect.width * scaling_factor)
        self.image = pygame.transform.scale(self.image, (self.target_width, self.target_height))
        self.rect = self.image.get_rect()


        

    def _position_image(self):
        self.rect.x = 2*self.target_width
            
        self.rect.y = self.target_height
