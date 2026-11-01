# Exercise 1: Birthday Look-up

# Instructions

# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.

# My first option -birthdays={ 
#     'person1':{'name':'Oksana', 'birthday': '1999/02/15'},
#     'person2':{'name':'Aviv', 'birthday': '1999/03/03'},
#     'person3':{'name':'Alina', 'birthday': '2001/08/31'},
#     'person4':{'name':'Unknown', 'birthday': '2002/07/25'}
# }
# for person in birthdays:
#     print(f"Welcome {birthdays[person]['name']}")
# print("You can look up the birthdays of the people in the list!")
# answer=input("Give me a person's name? ")
# answer.capitalize()
# for person in birthdays:
#     if answer == birthdays[person]['name']:
#         print (f"The birthday of {answer} is {birthdays[person]['birthday']}")

# Correct answers -birthdays = {
#     'Oksana': '1999/02/15',
#     'Aviv': '1999/03/03',
#     'Alina': '2001/08/31',
#     'Unknown': '2002/07/25',
#     'Maya': '2000/11/10'
# }

# print("Welcome!")
# print("You can look up the birthdays of the people in the list!")

# answer = input("Give me a person's name? ")
# answer = answer.capitalize()

# if answer in birthdays:
#     print(f"The birthday of {answer} is {birthdays[answer]}")
# else:
#     print(f"Sorry, I don't have {answer} in my list.")

# Exercise 2: Birthdays Advanced

# Instructions

# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

birthdays = {
    'Oksana': '1999/02/15',
    'Aviv': '1999/03/03',
    'Alina': '2001/08/31',
    'Unknown': '2002/07/25',
    'Maya': '2000/11/10'
}

# print("Welcome!")
# print("You can look up the birthdays of the people in the list!")

# print("Names are:")
# for name in birthdays:
#     print(name)
# answer = input("Give me a person's name? ")
# answer = answer.capitalize()

# if answer in birthdays:
#     print(f"The birthday of {answer} is {birthdays[answer]}")
# else:
#     print(f"Sorry, we don’t have the birthday information for {answer}")

# Exercise 3: Add Your Own Birthday

# Instructions

# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

your_name = input("Give me your name? ")
your_name = your_name.capitalize()
your_birthday=input("Give me birthday in the format YYYY/MM/DD: ")
birthdays.update({"your_name": "your_birthday"})
print("Names are:")
for name in birthdays:
    print(name)
answer = input("Give me a person's name? ")
answer = answer.capitalize()

if answer in birthdays:
    print(f"The birthday of {answer} is {birthdays[answer]}")
else:
    print(f"Sorry, we don’t have the birthday information for {answer}")


# Exercise 4: Fruit Shop
# Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
# sentence = "Items and their prices are: "
# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# for item in items:
#     sentence = sentence + item + ": " + str(items[item]) + "; "
# print(sentence)

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}}

total_cost = 0

for item in items:
    price_of_item = items[item]["price"] * items[item]["stock"]
    print(f"{item}: {price_of_item}")
    total_cost = total_cost + price_of_item

print(f"Total cost to buy everything in stock: {total_cost}")