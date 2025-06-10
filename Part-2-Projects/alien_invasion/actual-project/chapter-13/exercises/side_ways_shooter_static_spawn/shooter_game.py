import pygame
import sys
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
        star_width = star.rect.width
        star_height = star.rect.height

        current_x = star.rect.x
        current_y = star.rect.y
        sixty_percent_of_game_screen = 0.6 * (self.settings.screen.get_rect().width)
        print(self.settings.screen.get_rect().right)
        print(self.ship.image.get_rect().right)
        while current_x > sixty_percent_of_game_screen:
            while current_y >= 2*star_height:
                new_star = Star(self)
                new_star.rect.x = current_x
                new_star.rect.y = current_y
                self.stars.add(new_star)
                current_y -= 2*star_height
            current_x -= 2*star_width
            current_y = star.rect.y
        self.stars.add(star)

        

if __name__ == "__main__":
    game = SideWaysShooter()
    game.run_game()
