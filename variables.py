import pygame

#Measures
WINDOW_SIZE = 800
WIDTH, HEIGHT = WINDOW_SIZE, WINDOW_SIZE
WINDOW_SCALE = 2
SPRITE_SIZE = WINDOW_SIZE // 200

#Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Colors
BLACK = (0, 0, 0)
GREEN = (15, 210, 45)

#Sprites
green_pixel = pygame.Surface([SPRITE_SIZE, SPRITE_SIZE])
green_pixel.fill(GREEN)
