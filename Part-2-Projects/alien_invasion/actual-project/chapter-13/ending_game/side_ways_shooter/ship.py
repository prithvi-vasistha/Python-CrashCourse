import pygame
from settings import Settings

class Ship:
    def __init__(self, shooter):
        self.game = shooter
        self.settings = self.game.settings
        self.game_screen = self.settings.screen
        self.image = pygame.image.load("images/ship.bmp")
        self.image = self._rotate_image()
        self._set_position_image()
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False


    def get_positions(self):
        return(self.rect, self.game_screen_size)


    def _set_position_image(self):
        self.rect = self.image.get_rect()
        self.game_screen_size = self.game_screen.get_rect()
        self.rect.midleft = self.game_screen_size.midleft

    def load_image(self):
        if self.moving_up and self.rect.y > self.game_screen_size.y:
            self.y = float(self.rect.y)
            self.y -= self.settings.movement_area
            self.rect.y = self.y
        elif self.moving_down and self.rect.bottom < self.game_screen_size.bottom:
            self.y = float(self.rect.y)
            self.y += self.settings.movement_area
            self.rect.y = self.y
        elif self.moving_left and self.rect.left > self.game_screen_size.left:
            self.x = float(self.rect.x)
            self.x -= self.settings.movement_area
            self.rect.x = self.x
        elif self.moving_right and self.rect.right < self.game_screen_size.right:
            self.x = float(self.rect.x)
            self.x += self.settings.movement_area
            self.rect.x = self.x

        self.game_screen.blit(self.image, self.rect)

    def _rotate_image(self):
        self.location = self.image.get_rect().center
        rotated_image = pygame.transform.rotate(self.image, 270)
        rotated_image.get_rect().center = self.location
        return rotated_image 

    def center_ship(self):
        self.rect.midleft = self.game_screen.get_rect().midleft


