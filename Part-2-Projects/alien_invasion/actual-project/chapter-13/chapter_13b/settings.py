import pygame

class Settings:
    """ this is a class to store all the game settings """
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.color = (230,230,230)
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        self.alien_movement_speed = 1

