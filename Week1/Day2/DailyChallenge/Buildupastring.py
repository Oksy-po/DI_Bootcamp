# Instructions:

# 1. Ask for User Input:

# The string must be exactly 10 characters long.
# 2. Check the Length of the String:

# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 3. Print the First and Last Characters:

# Once the string is validated, print the first and last characters.
# 4. Build the String Character by Character:

# Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
# Hint: You can create a loop that goes through the string, adding one character at a time, and print it progressively.

# user_answer=input("Write a phrase and it should be exactly 10 characters long: ")
# if len(user_answer) <10:
#     print("String not long enough.")
# elif len(user_answer) >10:
#     print("String too long.")
# else:
#     print("Perfect string")
#     print(f"First character is {user_answer[0]} and last character is {user_answer[-1]}")
#     part = ""
#     for character in user_answer:
#         part += character
#         print(part)
import random  

user_answer = input("Write a phrase that is exactly 10 characters long: ")
length = len(user_answer)

if length < 10:
    print("String not long enough.")
elif length > 10:
    print("String too long.")
else:
    print("Perfect string")
    print(f"First character is {user_answer[0]} and last character is {user_answer[-1]}")

    part = ""
    for character in user_answer:
        part += character
        print(part)      

    list_of_letters=list(user_answer)
    random.shuffle(list_of_letters)
    new_line=list_of_letters
    shuffled_line= "".join(new_line)
    print(shuffled_line)

        
        
          
