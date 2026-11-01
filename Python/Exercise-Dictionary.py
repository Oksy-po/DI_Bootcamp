# Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).

# 2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.

# 3. Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).

# 4. Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. You should return something like this:

import string
information=[("name", "Elie"), ("job", "Instructor")]
new_information=dict(information)
print(new_information)

abbreviation=["CA", "NJ", "RI"]
cities=["California", "New Jersey", "Rhode Island"]
matched_city=dict(zip(abbreviation, cities))
print(matched_city)


# Not according task 
# vowels=['a', 'e', 'i', 'o', 'u']
# alphabet=dict.fromkeys(vowels,0)
# print(alphabet)

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_dict = {}
for vowel in vowels:
    vowel_dict[vowel] = 0
print(vowel_dict)   # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


letter_number = {}
for i, letter in enumerate(string.ascii_uppercase):
    letter_number[i+1] =letter

for i,letter in letter_number.items():
    print(i,letter)


# Given the string "awesome sauce", return a dictionary where the keys are vowels, and the values are the count of each vowel in the string. Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.


word = "awesome sauce"
vowels = "aeiou"

vowel_count = {}
for vowel in vowels:
    vowel_count[vowel] = 0        # start all vowels at 0 (so 'i' is included)

for letter in word:
    if letter in vowel_count:
        vowel_count[letter] += 1  # found one: add 1

print(vowel_count)   # {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}