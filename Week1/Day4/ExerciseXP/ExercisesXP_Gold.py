# Exercise 1 : Hello World-I love Python
# Instructions
# Print the following output in one line of code:
print("Hello World \n" *4 + "I love Python \n"*4)

# Exercise 2 : What is the Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)
try:
    month=int(input("Give me please a month (1 to 12)"))
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if month in (3,4,5):
        print("Okay,it is Spring")
    elif month in (6,7,8):
        print("Okay,it is Summer")
    elif month in (9,10,11):
        print("Okay,it is Autumn")
    elif month in (12,1,2):
        print("Okay,it is Winter")
except ValueError as e:
    print(e)

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.'''
print(len(my_text))

# Exercise 5: Longest word without a specific character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.
longest_sentence = ""
while True:
    sentence = input("Enter a sentence without the letter 'A': ")

    if "a" in sentence.lower():
        print("Oops! Your sentence contains the letter A.")
        continue

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You have a new longest sentence!")
        print(f"Length: {len(longest_sentence)}")
    elif len(sentence)<len(longest_sentence) or len(sentence) == len(longest_sentence):
        print("Ooops, it is not longer than previous")
    answer = input("Do you want to continue? (yes/no): ")
    if answer.lower() == "no":
        break