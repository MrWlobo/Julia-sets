import pygame
from variables import WIDTH, HEIGHT, WIN, SQUARE_SIZE,GREEN, PADDING, green_pixel, bottom_surface, chosen_values
from julia_set import output, select_point

pygame.display.set_caption("Julia sets displayer")
pygame.font.init()

#Display green sprite for every point that is in the set
def value_choice():
    index = 0
    for char in output:
        if char != ".":
            WIN.blit(green_pixel, (int(index) % int(WIDTH), index // WIDTH))
        index += SQUARE_SIZE

def display_chosen_value():
    font = pygame.font.SysFont('msminchomspmincho', HEIGHT // 16)
    WIN.blit(bottom_surface, (0, HEIGHT))
    real_value = font.render(f"Real value: {chosen_values[0]}", True, (GREEN))
    imaginary_value = font.render(f"Imaginary value: {chosen_values[1]}", True, (GREEN))
    WIN.blit(real_value, (0, HEIGHT + PADDING))
    WIN.blit(imaginary_value, (0, HEIGHT + 6 * PADDING))

#Update changes on app window
def update(event):
    select_point(event)
    value_choice()
    display_chosen_value()
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