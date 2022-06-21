import pygame
from variables import WIDTH, HEIGHT, WINDOW_SCALE, WIN, WINDOW_SIZE, BLACK

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
BASE_VALUE = WINDOW_SIZE * 2
values = []
imaginary_value = BASE_VALUE
real_value = -1 * BASE_VALUE
change_value = WINDOW_SCALE * 8
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

def create_julia_set(value, complex_value):
    z = complex(value[0]/BASE_VALUE*2, value[1]/BASE_VALUE*2) #Check for every pixel
    is_in_set = False
    solutions = []

    while is_in_set == False:
        solution = (z*z) + complex_value

        if solution.real >= 2 or solution.imag >= 2:
            #Point is not in set
            output.append(".")
            break

        # Point might be in set
        if len(solutions) > 6:
            output.append("1")
            break

        z = solution

        for sol in solutions:
            if sol == solution:
                #Point is in set
                is_in_set = True
                output.append("1")
        solutions.append(solution)

def select_point(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            WIN.fill(BLACK)
            output.clear()
            complex_value = complex(float(2*mouse_position[0]/WINDOW_SIZE - 1), float(-2*(mouse_position[1]/WINDOW_SIZE) + 1))

            #Displays anwser and write it to text file
            for value in values:
                create_julia_set(value, complex_value)
