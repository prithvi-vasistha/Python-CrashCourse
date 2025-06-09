import pygame
import sys
from settings import Settings 
from ship import Ship
from bullet import Bullet

class SideWaysShooter:
    def __init__(self):
        pygame.init()
        self.settings = Settings(self)
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
        
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                self._react_to_events(event)
            self.settings.screen.fill(self.settings.screen_color)
            self.ship.load_image()
            self._update_bullets()
            self._delete_old_bullets()
            self.clock.tick(60)
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
                print("removed bullet successfully")

if __name__ == "__main__":
    game = SideWaysShooter()
    game.run_game()
