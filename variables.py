import pygame

#Measures
WIDTH, HEIGHT = 400, 400
WINDOW_SCALE = 4

#Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Sprites
black_pixel = pygame.Surface([16, 16])
black_pixel.fill(WHITE)
