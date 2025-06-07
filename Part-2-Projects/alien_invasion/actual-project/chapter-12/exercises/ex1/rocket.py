import pygame

class Rocket:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        try:
            self.image = pygame.image.load("/home/ppv/Documents/ppv-skill-dev/python/codes/github/Python-CrashCourse/Part-2-Projects/alien_invasion/actual-project/chapter-12/exercises/images/ship.bmp")
            self.image_rect = self.image.get_rect()
        except Exception as e:
            print(e)
            print(self.screen_rect)
            print(self.image_rect)

        self.image_rect.center = self.screen_rect.center
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.move_up = False

    def update_image(self):
        self.screen.blit(self.image,self.image_rect)

    def handle_movement(self):
        if self.move_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.x += 1

        elif self.move_left and self.image_rect.left > self.screen_rect.left:
            self.image_rect.x -= 1

        elif self.move_up and self.image_rect.top > self.screen_rect.top:
            self.image_rect.y -= 1

        elif self.move_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += 1

