import pygame
from variables import WIDTH, HEIGHT, WINDOW_SCALE, WIN, BLACK

#Positions of pixels
pixels = []
real_number, imaginary_number = 0, 0 #Position X, Position Y

#Give every pixel a positiom
for i in range(WIDTH // WINDOW_SCALE * HEIGHT // WINDOW_SCALE):
    pixels.append((real_number, imaginary_number))
    real_number += 1
    if real_number == WIDTH:
        real_number = 0
        imaginary_number += 1

#Imaginary and real values of pixels
BASE_VALUE = 200
values = []
imaginary_value = BASE_VALUE
real_value = -1 * BASE_VALUE
change_value = 16
iterations = 0

for pixel in pixels:
    values.append((real_value, imaginary_value))
    real_value += change_value
    iterations += 1
    if iterations == WIDTH:
        iterations = 0
        real_value = -1 * BASE_VALUE
        imaginary_value -= change_value

output = []

def create_julia_set(value, c):
    z = complex(value[0]/BASE_VALUE*2, value[1]/BASE_VALUE*2) #Check for every pixel
    is_in_set = False
    solutions = []

    while is_in_set == False:
        solution = (z * z) + c

        if solution.real >= 2 or solution.imag >= 2:
            #Point is not in set
            output.append(".")
            break

        if len(solutions) > 5 and len(solutions) < 10:
            #Point might be in set
            output.append("o")
            break

        z = solution

        for sol in solutions:
            if sol == solution:
                #Point is in set
                is_in_set = True
                output.append("0")
        solutions.append(solution)

def select_point(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            WIN.fill(BLACK)
            output.clear()
            complex_value = complex(float(mouse_position[0]/BASE_VALUE - 1), float(-1 * (mouse_position[1]/BASE_VALUE - 1)))

            #Displays anwser and write it to text file
            for value in values:
                index = values.index(value)
                create_julia_set(value, complex_value)