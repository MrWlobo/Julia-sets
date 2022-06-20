import pygame
from variables import WIDTH, HEIGHT

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
main()