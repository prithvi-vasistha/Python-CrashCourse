import pygame

class Settings:
    """ this is a class to store all the game settings """
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.color = (230,230,230)
        self.ship_speed = 4
        self.bullet_speed = 4
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        self.alien_movement_speed = 1
        #original drop speed = 10
        self.fleet_drop_speed = 80

        # fleet_direction 1 = right; fleet_direction -1 = left
        self.fleet_direction = 1
        self.ships_remaining = 3
