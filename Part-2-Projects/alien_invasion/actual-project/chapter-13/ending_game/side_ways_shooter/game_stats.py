import pygame

class GameStats:
    def __init__(self, shooter_game):
        self.settings = shooter_game.settings
        self.reset_stats()


    def reset_stats(self):
        self.ship_lives = self.settings.ship_lives

