# Exercise 1: Lists
# Instructions

# Write Python code to complete the following tasks.

# Given a list [1, 2, 3, 4], print out all the values in the list one by one.

# Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.

# Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].

# Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].

# Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].

# Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].

# Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].

# For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].

# Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].

# Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].


first_numbers=[1, 2, 3, 4]
for item in first_numbers:
    print (item)

for item in first_numbers:
    new_item=item * 20
    print(new_item)

names=["Elie", "Tim", "Matt"]
new_names=[]
for name in names:
    new_name=name[0]
    new_names.append(new_name)
print(new_names)

numbers=[1, 2, 3, 4, 5, 6]
even_numbers=[]
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

list_1=[1, 2, 3, 4] 
list_2=[3, 4, 5, 6]
# My mistake 
# general_list=list_1+list_2
# for num in general_list:
#     if general_list.count(num) >1 and num not in updated_list:
#         updated_list.append(num)
# print(updated_list)


common_numbers = []
for num in list_1:
    if num in list_2 and num not in common_numbers:
        common_numbers.append(num)
print(common_numbers)   # [3, 4]

updated_names = []
for name in names:
    small = name.lower()        # "Elie" -> "elie"
    backwards = small[::-1]     # "elie" -> "eile"
    updated_names.append(backwards)

print(updated_names)   # ['eile', 'mit', 'ttam']

one_string="first"
second_string="third"
common_1=list(one_string)
common_2=list(second_string)
# My Mistake 
# common=common_1 + common_2
# for letter in common:
#     if common.count(letter) >1 and letter not in updated_common:
#         updated_common.append(letter)
# print(updated_common)

common_letters = []
for letter in one_string:
    if letter in second_string and letter not in common_letters:
        common_letters.append(letter)
print(common_letters)   # ['i', 'r', 't']


divisile_numbers=[]
for i in range(1,101):
    if i % 12 ==0:
        divisile_numbers.append(i)
print(divisile_numbers)

# My Mistake
# word="amazing"
# new_word=("amazing")
# vowels = "aeiou"
# new_vowels=("aeiou")
# updated_word=[]
# for letter in new_word:
#     if letter not in new_vowels:
#         updated_word.append(letter)
    
# print(updated_word)

word = "amazing"
vowels = "aeiou"
no_vowels = []
for letter in word:
    if letter not in vowels:
        no_vowels.append(letter)
print(no_vowels)   # ['m', 'z', 'n', 'g']


# My Mistake
# original=[0, 1, 2]
# final=[]
# for i in range(3):
#     original.copy()
#     final.append(original)
# print(final)

final = []
for i in range(3):
    final.append([0, 1, 2])
print(final)

# My Mistake
# original_2=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# final_2=[]

# for i in range(10):
#     original_2.copy()
#     final_2.append(original_2)
# for row in final_2:
#     print(row)

final_2=[]
for i in range(10):
    final.append([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for row in final_2:
    print(row)