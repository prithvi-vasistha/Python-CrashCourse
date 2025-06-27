""" This hold most of the important settings for the sideways shooter game """
import pygame

class Settings:
    def __init__(self, shooter_game):
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Sideway Shooter Game (ik it sounds like drugs)")
        self.screen_color = (230,230,230)
        self.movement_area = 3.5
        self.bullet_size = (0,0,7,5)
        self.bullet_color = (0,0,0)
        self.bullet_speed = 6.5
        self.amount_bullets = 5
        self.alien_move_left = 100
        self.alien_move_up_down = 1.5
        self.ship_lives = 3


