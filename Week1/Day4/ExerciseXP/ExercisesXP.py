# Exercise 1: Favorite Numbers
# Key Python Topics:
# Sets
# Adding/removing items in a set
# Set concatenation (using union)
my_fav_numbers={1,6,8,7}
my_fav_numbers.update([2,10])
print(my_fav_numbers)
my_fav_numbers.remove(2)
print(my_fav_numbers)
friend_fav_numbers={6,5,11}
print(friend_fav_numbers)
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2: Tuple
# Key Python Topics:
# Tuples (immutability)
# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
numbers=(1,2,3,4)
numbers.append(1)  # AttributeError: 'tuple' object has no attribute 'append'

# Exercise 3: List Manipulation
# Key Python Topics:
# Lists
# List methods: append, remove, insert, count, clear
# Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

# Exercise 4: Floats
# Key Python Topics:
# Lists
# Floats and integers
# Range generation
# Instructions:
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?
numbers = [i / 2 if i % 2 != 0 else i // 2 for i in range(3, 11)]
print(numbers)

# Exercise 5: For Loop
# Key Python Topics:
# Loops (for)
# Range and indexing
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

r=range(1,21) 
for i in r:
    print(i)
for index, number in enumerate(r):
    if index % 2 == 0:
        print(number)

# Exercise 6: While Loop
# Key Python Topics:
# Loops (while)
# Conditionals
# Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

while True:
    user_name=input("What is your name? ")
    if user_name.isdigit() or len(user_name) <3:
        print("Please give correct name.It should not include digits and to have more than 3 letters")
        continue
    print("Thank You")
    break

# Exercise 7: Favorite Fruits
# Key Python Topics:
# Input/output
# Strings and lists
# Conditionals
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

favorite_fruits = input("Give me your favorite fruits: ").split()
print(favorite_fruits)
fruit = input("Give me one fruit: ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings
# Key Python Topics:
# Loops
# Lists
# String formatting
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

pizza_toppings = []
while True:
    topping = input("Please enter a pizza topping: ")
    if topping.lower() == "quit":
        break
    print(f"Adding {topping} to your pizza.")
    pizza_toppings.append(topping)

price = 10 + len(pizza_toppings) * 2.50
print(f"Toppings: {pizza_toppings}")
print(f"Total cost: ${price}")    

# Exercise 9: Cinemax Tickets
# Key Python Topics
# Conditionals
# Lists
# Loops
# Instructions
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_cost = 0
family_members = input("Give me your names: ").split()
for member in family_members:
    age = int(input(f"What is {member}'s age? "))

    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print(f"Total ticket cost: ${total_cost}")

# Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

teenagers = input("Give me your names: ").split()
allowed = []
for member in teenagers:
    age = int(input(f"What is {member}'s age? "))

    if 16 <= age <= 21:
        allowed.append(member)

print(f"Here is the list: {allowed}")






        
        
            
        


