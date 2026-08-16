# text = "Python is Fun!"
# new_text=text.upper()
# print(new_text)
# only_first_letter=text.capitalize()
# print(only_first_letter)
# all_words=text.title()
# print(all_words)
# f=text.find("F")
# print(f)
# print("is" in text)
# your_print=input("Give me your sentence: ")
# your_print.isalpha()
# your_print.endswith("!")
# your_print.isspace()

# # Step 1: Ask the user to input a sentence
# sentence = input("Enter a sentence: ")

# # Step 2: Check if the sentence contains only alphabetic characters
# if sentence.isalpha():
#     print("The sentence contains only alphabetic characters.")
# else:
#     non_alpha_count = len([char for char in sentence if not char.isalpha()])
#     print(f"The sentence contains {non_alpha_count} non-alphabetic characters.")

# # Step 3: Determine if the sentence ends with an exclamation mark
# if sentence.endswith('!'):
#     print("The sentence ends with an exclamation mark.")
# else:
#     print("The sentence does not end with an exclamation mark.")

# # Step 4: Find if the sentence contains any whitespace characters
# if sentence.isspace():
#     print("The sentence contains only whitespace characters.")
# elif any(char.isspace() for char in sentence):
#     print("The sentence contains some whitespace characters.")
# else:
#     print("The sentence contains no whitespace characters.")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])
print(fruits[2])
fruits[1]="blueberry"
print(fruits)
fruits.append("fig")
fruits.insert(0,"grape")
fruits.remove("cherry")
fruits.pop()
combined_list=fruits.extend(["strawberry","rasberry"])
combined_list.sort()
combined_list[4:]
# Given list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 1. Add "fig" to the end of the fruits
fruits.append("fig")
print(fruits)

# 2. Insert "grape" at the beginning of the list
fruits.insert(0, "grape")
print(fruits)

# 3. Remove "cherry" from the list using the specific method for it
fruits.remove("cherry")
print(fruits)

# 4. Remove the last element from the list using the specific method for it
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

# 5. Create another list of berries and combine it with the fruits list into a list called "combined_list"
berries = ["strawberry", "raspberry", "blueberry"]
combined_list = fruits + berries
print(combined_list)

# 6. Sort the combined_list
combined_list.sort()
print(combined_list)

# 7. Slice the last three elements of the combined list
last_three = combined_list[-3:]
print(last_three) 


