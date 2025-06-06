import pygame

class Ship:
    def __init__(self, ai_game):
        self.surface = ai_game.surface
        # get the screen size of the ai_game
        self.surface_rect = ai_game.surface.get_rect()

        # enable continuous movement
        self.moving_right = False
        
        self.image = pygame.image.load("/home/ppv/Documents/ppv-skill-dev/python/codes/github/Python-CrashCourse/Part-2-Projects/alien_invasion/actual-project/chapter-16-pilot_ship/images/ship.bmp")
    

        # loads the image size
        self.rect = self.image.get_rect()
        og_width,og_height = self.surface.get_size()
        image_width, image_height = self.image.get_size()
        target_height = int(0.15*og_height)
        scale_factor = target_height/image_height
        target_width = int(scale_factor*image_width)
        scaled_image = pygame.transform.scale(self.image,(target_width,target_height))

        self.rect = scaled_image.get_rect()

        self.rect.midbottom = self.surface_rect.midbottom


    def loadBlit(self, ai_game):
        self.rect = self.image.get_rect()
        self.surface_rect = ai_game.surface.get_rect()
        self.rect.midbottom = self.surface_rect.midbottom
        self.surface.blit(self.image, self.rect)

    def update(self):
        """ update the ship's position based on my movement flag self.moving_right """
        self.rect.x+=1

