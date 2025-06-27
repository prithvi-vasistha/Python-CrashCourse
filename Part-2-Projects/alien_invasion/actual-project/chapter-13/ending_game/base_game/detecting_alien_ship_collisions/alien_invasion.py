import pygame
import sys
import random   
from time import sleep
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self._create_fleet()
        self._initialize_first_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        else:
            pass

    def _delete_old_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_bullets(self):
        self.bullets.update(self.bullet_speed)
        self._delete_old_bullets()

        #check for collisions of bullets and aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._set_values_for_next_fleet()
            self._create_fleet()

    def _update_screen(self):
        self.screen.fill(self.settings.color)
        for bullet in self.bullets.sprites(): bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        pygame.display.flip()

    def _create_fleet(self):
        # Goal: create an alien and keep adding alien till the end of the screen
        # The space between each alien is of one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._add_new_alien(current_x, current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2*alien_height
        self.aliens.add(alien)

    def _add_new_alien(self, current_x, current_y):
        new_alien = Alien(self)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        new_alien.rect.y = current_y
        self.aliens.add(new_alien)

    def _update_alien(self):
        self._check_alien_fleet_edges()
        self.aliens.update()
        
        # look for alien ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
    def _check_alien_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _set_values_for_next_fleet(self):
        self.alien_movement_speed *= 1.5
        self.fleet_drop_speed = random.randrange(1,30)  
        # random_bullet_speed_seed = random.randrange(100,200)
        # random_bullet_speed_seed /= 100
        # self.bullet_speed *= random_bullet_speed_seed
        self.bullet_speed = self.alien_movement_speed

        print(f"alien_movement_speed : {self.alien_movement_speed} ")
        print(f"fleet_drop_speed :{self.fleet_drop_speed}") 
        print(f"bullet_speed :{self.bullet_speed}") 


        #cap alien_movement_speed at 10
        if self.alien_movement_speed > 12:
            self.alien_movement_speed = 12
    

    def _initialize_first_fleet(self):
        self.alien_movement_speed = self.settings.alien_movement_speed
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        self.bullet_speed = self.settings.bullet_speed

    def _ship_hit(self):
        self.stats.ships_left -= 1
        self.bullets.empty()
        self.aliens.empty()

        #create a new fleet
        self._create_fleet()
        self.ship.center_ship()
        sleep(0.5)


if __name__ == "__main__":
    alien = AlienInvasion()
    alien.run_game()
