import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((400,600), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                pygame.display.flip()
                self.clock.tick(60)


if __name__ == "__main__":
    alien = AlienInvasion()
    alien.run_game()
