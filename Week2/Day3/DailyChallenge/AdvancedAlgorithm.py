# Instructions

# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

# For example

# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728

import random 

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

# for i in range(len(list_of_numbers)):
#     for j in range(i+1, len(list_of_numbers)):
#         if list_of_numbers[i] + list_of_numbers[j] == target_number:
#             print ( f"{list_of_numbers[i]} and {list_of_numbers[j]} sums to the target_number {target_number}")
        

unique_numbers=set(list_of_numbers)
for number in unique_numbers:
    second_number=target_number-number
    if second_number in unique_numbers and number > second_number:
        print ( f"{number} and {second_number} sums to the target_number {target_number}")

    # Situation 2: the SAME number twice (like 1864 + 1864)
    if number == second_number and list_of_numbers.count(number) >= 2:
        print(f"{number} and {second_number} sums to the target_number {target_number}")
    