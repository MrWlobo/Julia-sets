import pygame
from variables import WIDTH, WIN, black_pixel
from julia_set import output, select_point

pygame.display.set_caption("Julia sets displayer")

def value_choice():
    index = 0
    for char in output:
        if char != ".":
            WIN.blit(black_pixel, (int(index) % int(WIDTH), index // WIDTH))
        index += 15

def update(event):
    select_point(event)
    value_choice()
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update(event)
    pygame.quit()
main()