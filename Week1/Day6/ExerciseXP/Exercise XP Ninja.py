# Exercise 1 : Cars

# Instructions

# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

string="Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
my_list=string.split(", ")
print(my_list)
print(f"Manufacturers/companies are {len(my_list)} in the list")
my_list.sort(reverse=True)
print(my_list)
# Count names containing "o"
count_with_o = 0
for name in my_list:
    if "o" in name:
        count_with_o = count_with_o + 1

print(f"Manufacturers with the letter 'o': {count_with_o}")

# Count names without "i"
count_without_i = 0
for name in my_list:
    if "i" not in name:
        count_without_i = count_without_i + 1

print(f"Manufacturers without the letter 'i': {count_without_i}")

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
no_duplications=set(my_list)
new_list=list(no_duplications)
result = ", ".join(new_list)
print(new_list)

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
new_list.sort()
reversed_names = []
for item in new_list:
    reversed_names.append(item[::-1])

result = ", ".join(reversed_names)
print(result)