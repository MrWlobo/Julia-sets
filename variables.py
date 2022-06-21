import pygame

#Measures
WINDOW_SIZE = 800
WIDTH, HEIGHT, BOTTOM_SURFACE_HEIGHT = WINDOW_SIZE, WINDOW_SIZE, WINDOW_SIZE // 8
WINDOW_SCALE = 2
SQUARE_SIZE = WINDOW_SIZE // 200
PADDING = 10

#Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT + BOTTOM_SURFACE_HEIGHT))

#Colors
BLACK = (0, 0, 0)
GREEN = (15, 210, 45)
GREY = (45, 45, 45)

#Sprites
green_pixel = pygame.Surface([SQUARE_SIZE, SQUARE_SIZE])
green_pixel.fill(GREEN)
bottom_surface = pygame.Surface([WIDTH, BOTTOM_SURFACE_HEIGHT])
bottom_surface.fill(GREY)

#Chosen values
chosen_values = ["-", "-"]