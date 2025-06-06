import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("/home/ppv/Documents/ppv-skill-dev/python/codes/github/Python-CrashCourse/Part-2-Projects/alien_invasion/actual-project/chapter-16-pilot_ship/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x+=1
        elif self.moving_left:
            self.rect.x-=1

