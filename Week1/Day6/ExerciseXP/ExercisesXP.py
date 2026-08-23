# Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:
# Creating dictionaries
# Zip function or dictionary comprehension
# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
# Lists:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = {}
for keys, value in zip(keys, values):
    dictionary[keys] = value
print(dictionary)

# Exercise 2: Cinemax #2
# Key Python Topics:
# Looping through dictionaries
# Conditionals
# Calculations
# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $1
# Family Data:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.
total_cost=0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for key,age in family.items():
    age=int(value)
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
        
    total_cost += cost
    print(f"Cost of {key} is ${cost}")
print(f"Total ticket cost: ${total_cost}")

# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {}
number_of_members = int(input("How many family members? "))
for i in range(number_of_members):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    family[name] = age
print(family)
for key,age in family.items():
    age=int(value)
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
        
    total_cost += cost
    print(f"Cost of {key} is ${cost}")
print(f"Total ticket cost: ${total_cost}")

# Exercise 3: Zara
# Key Python Topics:
# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()
# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}
# Change number_stores to 2
brand['number_stores'] = 2
# Print a sentence describing Zara's clients
print(f"Zara's clients are: {brand['type_of_clothes']}")
# Add country_creation
brand['country_creation'] = 'Spain'
# Check if international_competitors exists, then add Desigual
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
# Delete creation_date
brand.pop('creation_date')
# Print the last item in international_competitors
print(brand['international_competitors'][-1])
# Print major colors in the US
print(brand['major_color']['US'])
# Print number of keys
print(len(brand))
# Print all keys
print(brand.keys())

# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara ={
'creation_date':1975,
'number_stores':6998
}       
merged = brand | more_on_zara
print(merged)

# Exercise 4: Disney Characters
# Key Python Topics:
# Looping with indexes
# Dictionary creation
# Sorting
# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
user_indices = {}
for index, name in enumerate(users):
    user_indices[name] = index
print(user_indices)

# Create a dictionary that maps indices to characters:
user_indices2 = {}
for index, name in enumerate(users):
    user_indices2[index] = name
print(user_indices2)

# Create a dictionary where characters are sorted alphabetically and mapped to their indices:
user_indices3 = {}
for index, name in enumerate(users):
    user_indices3[name] = index
# Now build a NEW dictionary, sorted by key
sorted_dict = {}
for name in sorted(user_indices3):
    sorted_dict[name] = user_indices3[name]
print(sorted_dict)