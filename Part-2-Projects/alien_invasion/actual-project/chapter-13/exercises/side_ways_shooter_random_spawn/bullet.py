import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    def __init__(self, shooter_game):
        super().__init__()
        self.game_instance = shooter_game
        self.screen = self.game_instance.settings.screen
        self.settings = self.game_instance.settings
        self.ship_size, self.game_screen_size = self.game_instance.ship.get_positions()
        self.bullet = pygame.Rect(self.settings.bullet_size) 
        self.bullet_color = self.settings.bullet_color

        self.bullet.midright = self.ship_size.midright
        self.x = float(self.bullet.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.bullet.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.bullet)
