import pygame
import sys
from rocket import Rocket

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,800),pygame.RESIZABLE)
        pygame.display.set_caption("This is a sample movement game")
        self.color = (230,230,230)
        self.ship = Rocket(self)
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._handle_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._handle_keyup_events(event)

            self._update_game_screen()
            self.clock.tick(60)


        

    def _update_game_screen(self):
        self.screen.fill(self.color)
        self.ship.update_image()
        self.ship.handle_movement()
        self.ship.update_image()
        pygame.display.flip()



    def _handle_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True

        elif event.key == pygame.K_UP:
            self.ship.move_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        else:
            pass

    def _handle_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

        elif event.key == pygame.K_UP:
            self.ship.move_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False
        else:
            pass


if __name__ == "__main__":
    game = Game()
    game.run_game()
