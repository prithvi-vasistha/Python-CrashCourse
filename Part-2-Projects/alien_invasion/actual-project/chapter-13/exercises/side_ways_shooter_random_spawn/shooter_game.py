import pygame
import sys
import random
from settings import Settings 
from ship import Ship
from bullet import Bullet
from star import Star

class SideWaysShooter:
    def __init__(self):
        pygame.init()
        self.settings = Settings(self)
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self._draw_stars()
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                self._react_to_events(event)
            self.settings.screen.fill(self.settings.screen_color)
            self.stars.draw(self.settings.screen)
            self.ship.load_image()
            self._update_bullets()
            self._delete_old_bullets()
            self.clock.tick(120)
            pygame.display.flip()

    def _react_to_events(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit() 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_SPACE:
            self._add_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _add_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _delete_old_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.bullet.right >  self.settings.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _draw_stars(self):
        star = Star(self)
        screen_size = self.settings.screen.get_rect()
        fourty_percent_of_the_screen = 0.6*screen_size.width
        star_width = star.rect.width
        star_height = star.rect.height
        current_y = star_height
        current_x = star_width
        
        count = 10
        while count >= 0:
            new_star = Star(self)
            new_star.rect.x = random.randrange(int(fourty_percent_of_the_screen),int(screen_size.right - 2*new_star.rect.width))
            new_star.rect.y = random.randrange(screen_size.top + 2*star_height, screen_size.bottom - 2*star_height)
            self.stars.add(new_star)
            count -=1

        # print(fourty_percent_of_the_screen)
        # print(screen_size.right)
        # print(f"screen_size.bottom : {screen_size.bottom}")
        # print(f"screen_size.bottom - 2*star_height : {screen_size.bottom - 2*star_height}")
        # print(f"screen_size.top : {screen_size.top}")
        # print(f"screen_size.top + 2*star_height : {screen_size.top + 2*star_height}")



        

if __name__ == "__main__":
    game = SideWaysShooter()
    game.run_game()
