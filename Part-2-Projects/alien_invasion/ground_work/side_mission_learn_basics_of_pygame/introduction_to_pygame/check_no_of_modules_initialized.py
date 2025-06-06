import pygame

(numpass,numfail) = pygame.init()

print(f'Number of modules initialized successfully: {numpass}')
print(f'Number of modules failed to load: {numfail}')
