# Exercise 1: Concatenate lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# Exercise 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range(1500, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

# Exercise 3: Check the index
# Instructions
# Using this variable
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name=input("What is you name? ")
if user_name in names:
    print(names.index(user_name))

# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
# Test Data
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87
# The greatest number is: 87

first=int(input("Give me first number: "))
second=int(input("Give me second number: "))
third=int(input("Give me third number: "))
if first > second and first > third:
    print(f"The greatest number is:{first}")
elif second >first and second>third:
    print(f"The greatest number is:{second}")
else:
    print(f"The greatest number is: {third}")

# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

import string
alphabet = string.ascii_lowercase
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")

# Exercise 6: Words and letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

user_answer = input("Give me 7 words separated by spaces: ").split()
letter = input("Give me character: ")
for word in user_answer:
    if letter in word:
        print(word.index(letter))
    else:
        print(f"The letter {letter} is not in {word}")

# Exercise 7: Min, Max, Sum
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be:

numbers=input("Give me numbers and separate with comma: ").split(",")
list=list(numbers)
print(list)
tuple=tuple(list)
print(tuple)

# Exercise 9 : Random number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

wins = 0
losses = 0

while True:
    random_number = random.randint(1, 9)
    number = int(input("Give me a number from 1 to 9: "))

    if number == random_number:
        print("Winner!")
        wins += 1
    else:
        print("Better luck next time!")
        print(f"Sorry! The number was {random_number}")
        losses += 1

    answer = input("Write 'quit' if you want to exit: ")

    if answer == "quit":
        break

print(f"Games won: {wins}")
print(f"Games lost: {losses}")

# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:

C=50
H=30
D=input("Give me please numbers and separate with comma: ").split(",")
results=[]
for value in D:
    value=int(value)
    Q = ((2 * C * value)/H)**0.5
    results.append(Q)
print(results)

# Store the list of numbers in a variable.
# 2. Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers
# 3. A list containing the first and the last numbers.
# 4. A list of all the numbers greater than 50.
# 5. A list of all the numbers smaller than 10.
# 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# 7. The numbers without any duplicates – also print how many numbers are in the new list.
# 8. The average of all the numbers.
# 9. The largest number.
# 10.The smallest number.
# 11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
# 14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# 15. Bonus: Will the code work when the number of random numbers is not equal to 10?

import random
line1=[3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
line2=[44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
line3=[3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
line4=[18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# 2a. Print list in a single line
print(line1)

# 2b. Sorted descending
sorted_desc = sorted(line1, reverse=True)
print(sorted_desc)

# 2c. Sum
print(sum(line1))

# 3. First and last
first_last = [line1[0], line1[-1]]
print(first_last)

# 4. Greater than 50
greater_50 = []
for value in line1:
    if value > 50:
        greater_50.append(value)
print(greater_50)

# 5. Smaller than 10
smaller_10 = []
for value in line1:
    if value < 10:
        smaller_10.append(value)
print(smaller_10)

# 6. Squared
squared = []
for value in line1:
    squared.append(value ** 2)
print(squared)

# 7. No duplicates
no_duplicates = list(set(line1))
print(no_duplicates)
print("Count:", len(no_duplicates))

# 8. Average
average = sum(line1) / len(line1)
print("Average:", average)

# 9. Largest
print(max(line1))

# 10. Smallest
print(min(line1))

# 11. Bonus - without built-in functions
total = 0
for value in line1:
    total += value

manual_average = total / len(line1)

manual_max = line1[0]
manual_min = line1[0]
for value in line1:
    if value > manual_max:
        manual_max = value
    if value < manual_min:
        manual_min = value

print("Manual sum:", total)
print("Manual average:", manual_average)
print("Manual max:", manual_max)
print("Manual min:", manual_min)

# 12. Bonus - ask user for 10 numbers
numbers = []
for i in range(10):
    answer = int(input("Give me a number from -100 to 100: "))
    numbers.append(answer)
print(numbers)

# 13. Bonus - generate 10 random numbers instead
random_list = []
for x in range(10):
    random_number = random.randint(-100, 100)
    random_list.append(random_number)
print(random_list)

# Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
random_list = []
amount = random.randint(50, 100)

for x in range(amount):
    random_number = random.randint(-100, 100)
    random_list.append(random_number)

print(random_list)
print("How many numbers:", len(random_list))

# Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

paragraph = '''Python is a powerful and popular programming language used for web development, data science, automation, and artificial intelligence. It was created by Guido van Rossum and first released in 1991. One of the biggest reasons people love Python is its simple and readable syntax, which makes it a great choice for beginners. Despite being easy to learn, Python is also used by large companies for complex and demanding projects. Many popular tools and libraries, such as NumPy, Pandas, and Django, are built with Python.'''

# Characters
characters = len(paragraph)

# Sentences
sentences = paragraph.split(".")
sentences = [s for s in sentences if s.strip() != ""]

# Words
words = paragraph.split()

# Unique words (lowercased so "Python" and "python" count as the same word)
unique_words = set(word.lower() for word in words)

# Non-whitespace characters
count = 0
for char in paragraph:
    if char != " ":
        count += 1

# Average words per sentence
average = len(words) / len(sentences)

# Non-unique words
non_unique = len(words) - len(unique_words)

# Print nicely formatted results
print(f"Characters: {characters}")
print(f"Sentences: {len(sentences)}")
print(f"Words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Non-whitespace characters: {count}")
print(f"Average words per sentence: {average:.2f}")
print(f"Non-unique words: {non_unique}")

# Exercise 4 : Frequency Of The Words
# Instructions
# Write a program that prints the frequency of the words from the input
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1 

text=input("Give me your sentence")  
words = text.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
for word in sorted(frequency):
    print(f"{word}:{frequency[word]}")