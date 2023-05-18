# import numpy as np

import random

def generate_random_number():
    return random.randint(1, 10)

# # Generate a single random number
# random_number = generate_random_number()
# print("numero: ", random_number)

# if random_number % 2 == 0:
#     print("Le otto montagne")
# else:
#     print("Nanni Moretti")
# # print(random_number)

# Generate multiple random numbers
num_of_numbers = 11

random_numbers = [generate_random_number() for _ in range(num_of_numbers)]

otto_mont = 0
nanni = 0
for num in random_numbers:
    # otto montagne vince
    if num % 2 == 0:
        otto_mont += 1
    # nanni moretti vince
    else:
        nanni += 1

print("Nanni Moretti: ", nanni)
print("Otto Montagne: ", otto_mont)

print(random_numbers)