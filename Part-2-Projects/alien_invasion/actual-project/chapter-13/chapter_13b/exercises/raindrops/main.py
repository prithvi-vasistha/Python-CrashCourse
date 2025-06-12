import pygame
import sys
from settings import Settings
from raindrop import Raindrop

class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.raindrops = pygame.sprite.Group()
        self._render_screen()
        self.clock = pygame.time.Clock()

    def run_program(self):
        while True:
            self._react_to_events()
            self._update_screen()
            self.clock.tick(60)


    def _react_to_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _render_screen(self):
        self.settings.screen.fill(self.settings.bgcolor) 
        self._render_raindrops()
        pygame.display.flip()

    def _render_raindrops(self):
        raindrop = Raindrop(self)
        current_x = raindrop.rect.x
        current_y = raindrop.rect.y
        twenty_percent_of_game_screen = 0.2 * self.settings.screen.get_rect().height

        while current_y < twenty_percent_of_game_screen:
            while current_x < (self.settings.screen.get_rect().width - 2*raindrop.target_width):
                new_raindrop = Raindrop(self)
                new_raindrop.rect.x = current_x
                new_raindrop.rect.y = current_y
                self.raindrops.add(new_raindrop)
                current_x += new_raindrop.target_width
            current_x = raindrop.rect.x
            current_y += raindrop.target_height

    def _animate_raindrop_sprites(self):
        screen_bottom = self.settings.screen.get_rect().bottom
        for raindrop in self.raindrops: 
            if raindrop.rect.top < screen_bottom:
                raindrop.rect.y += 1
            else:
                raindrop.rect.y = raindrop.target_height
        

    def _update_screen(self):
        self.settings.screen.fill(self.settings.bgcolor)
        self.raindrops.draw(self.settings.screen)
        self._animate_raindrop_sprites()
        pygame.display.flip()

if __name__ == "__main__":
    program = Main()
    program.run_program()
