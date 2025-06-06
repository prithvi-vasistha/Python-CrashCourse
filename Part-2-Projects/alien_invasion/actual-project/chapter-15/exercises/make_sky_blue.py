import pygame
import sys

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((400,800),pygame.RESIZABLE)
        pygame.display.set_caption("Alien Invasion but sky blue sky")
        self.color = (0,181,226)
        self.image = pygame.image.load("images/goku.bmp")
        self.bgsize = self.surface.get_rect()
        self.gokuSize = self.image.get_rect()
        self.bgsize.midbottom = self.gokuSize.midbottom

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.bgsize = self.surface.get_rect()
        screen_width, screen_height = self.surface.get_size()
        img_width, img_height = self.image.get_size()

        # Calculate scale factor based on height to keep aspect ratio
        target_height = int(screen_height * 0.15)  
        scale_factor = target_height / img_height
        target_width = int(img_width * scale_factor)

        # Scale the image
        scaled_image = pygame.transform.scale(self.image, (target_width, target_height))

        # Get rect of scaled image and position at midbottom
        self.gokuSize = scaled_image.get_rect()
        self.gokuSize.midbottom = self.bgsize.midbottom

        # Fill background, blit scaled image, update display
        self.surface.fill(self.color)
        self.surface.blit(scaled_image, self.gokuSize)
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
