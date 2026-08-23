# Challenge 1: Multiples of a Number
# Key Python Topics:
# input() function
# Loops (for or while)
# Lists and appending items
# Basic arithmetic (multiplication)
# Instructions:
# 1. Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.
# Example 1:
# Input:
# number: 7
# length: 5
# Output:
# [7, 14, 21, 28, 35]

number = int(input("Give me the number: "))
length = int(input("Give me the length: "))
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)

# Challenge 2: Remove Consecutive Duplicate Letters
# Key Python Topics:
# input() function
# Strings and string manipulation
# Loops (for or while)
# Conditional statements (if)
# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

word = input("Give me a string: ")
result = ""
previous = ""
for letter in word:
    if letter != previous:
        result += letter
        previous = letter
print(result)

