# Exercise 1: Add Two Numbers
# Instructions

# Write a function add_two_numbers that takes two numbers as parameters and returns their sum.

import calendar
def add_two_numbers(number_1,number_2):
    """Return a sum of two numbers"""
    return number_1 + number_2

print(add_two_numbers(3,5))
print(add_two_numbers(10, 20))


# Exercise 2: Print a Greeting
# Instructions

# Write a function greet that takes one parameter, a person’s name, and prints a greeting message like “Hello, [name]!”.

def greet(name):
    """Return a greeting message."""
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")


# Exercise 3: Check if Number is Even or Odd
# Instructions

# Write a function check_even_odd that takes one number and prints “Even” if the number is even, and “Odd” if the number is odd.

def check_even_odd(a):
    
    if a %2 ==0:
        print("Even") 
    else:
        print("Odd")

check_even_odd(4)
check_even_odd(7)


# Exercise 4: Sum of Numbers in a List
# Instructions

# Write a function sum_list that takes a list of numbers as a parameter and returns the sum of all numbers in the list.

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4]))  # Output: 10
print(sum_list([5, 5, 5]))  # Output: 15


# Exercise 5: Print Days of the Week
# Instructions

# Write a function print_days that prints the days of the week (Sunday, Monday, Tuesday, etc.) using a loop.

def print_days():
    week=list(calendar.day_name)
    
    for day in week:
        print(day)


print_days()


# Exercise 6: Check if Number is Positive, Negative, or Zero
# Instructions

# Write a function check_sign that takes a number and prints whether the number is positive, negative, or zero.


def check_sign(b):
    
    if b >0:
        print("Positive")
    elif b <0:
        print("Negative")
    else:
        print("Zero")

check_sign(10)  # Output: "Positive"
check_sign(-5)  # Output: "Negative"
check_sign(0)   # Output: "Zero"


# Exercise 7: Repeat a Word
# Instructions

# Write a function repeat_word that takes a word and a number as parameters and prints the word that many times.

def repeat_word(word,number):
    for __ in range(number):
        print(word)


repeat_word("hello", 3)
# Output:
# hello
# hello
# hello

repeat_word("goodbye", 2)  
# Output:
# goodbye
# goodbye