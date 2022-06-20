#Positions of pixels
pixels = []
real_number, imaginary_number = 0, 0 #Position X, Position Y

#Give every pixel a positiom
for i in range(63001):
    pixels.append((real_number, imaginary_number))
    real_number += 1
    if real_number == 251:
        real_number = 0
        imaginary_number += 1

#Imaginary and real values of pixels
values = []
imaginary_value = 2000
real_value = -2000
change_value = 16
iterations = 0

for pixel in pixels:
    values.append((real_value, imaginary_value))
    real_value += change_value
    iterations += 1
    if iterations == 251:
        iterations = 0
        real_value = -2000
        imaginary_value -= change_value

output = []

def create_julia_set(value, c):
    z = complex(value[0]/1000, value[1]/1000) #Check for every pixel
    is_in_set = False
    solutions = []

    while is_in_set == False:
        solution = (z * z) + c

        if solution.real >= 2 or solution.imag >= 2:
            #Point is not in set
            output.append(".")
            break

        if len(solutions) > 10 and len(solutions) < 100:
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

print("Format: float + float") #Example: 0.24 + 0.45
complex_value_input = str(input())
complex_value_elements = complex_value_input.split()
complex_value = complex(float(complex_value_elements[0]), float(complex_value_elements[2]))

#Display anwser and write it to text file
for value in values:
    index = values.index(value)
    create_julia_set(value, complex_value)
    if len(output) == 251:
        for char in output:
            print(char, end="")
        print("\n")
        output.clear()

