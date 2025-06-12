import pygame
import sys
import random
from settings import Settings 
from ship import Ship
from bullet import Bullet
from alien import Alien

class SideWaysShooter:
    def __init__(self):
        pygame.init()
        self.settings = Settings(self)
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._draw_aliens()
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                self._react_to_events(event)
            self.settings.screen.fill(self.settings.screen_color)
            self.aliens.draw(self.settings.screen)
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

    def _draw_aliens(self):
        alien = Alien(self)
        screen_size = self.settings.screen.get_rect()
        fourty_percent_of_the_screen = 0.6*screen_size.width
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_y = alien_height
        current_x = alien_width
        
        count = 10
        while count >= 0:
            new_alien = Alien(self)
            new_alien.rect.x = random.randrange(int(fourty_percent_of_the_screen),int(screen_size.right - 2*new_alien.rect.width))
            new_alien.rect.y = random.randrange(screen_size.top + 2*alien_height, screen_size.bottom - 2*alien_height)
            self.aliens.add(new_alien)
            count -=1

        # print(fourty_percent_of_the_screen)
        # print(screen_size.right)
        # print(f"screen_size.bottom : {screen_size.bottom}")
        # print(f"screen_size.bottom - 2*alien_height : {screen_size.bottom - 2*alien_height}")
        # print(f"screen_size.top : {screen_size.top}")
        # print(f"screen_size.top + 2*alien_height : {screen_size.top + 2*alien_height}")



        

if __name__ == "__main__":
    game = SideWaysShooter()
    game.run_game()
