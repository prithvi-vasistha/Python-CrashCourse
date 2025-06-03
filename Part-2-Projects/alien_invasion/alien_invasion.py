import sys
import pygame

class AlienInvasion:
    """ Overall class to manage game assets and behaviour """    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion Game")

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            # watch for the keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                ''' make most recently drawn screen visible '''
                pygame.display.flip()
                
if __name__ == "__main__":
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

