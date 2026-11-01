# Exercise 1 : What’s your name ?

# Instructions

# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.


def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:        # true only if middle_name is not empty
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))


# Exercise 2 : From English to Morse

# Instructions

# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.


morse_code = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    " ": "/"      # common way to show a space between words
}
   
def converter_to_morse_code(text):
    converted = []
    for letter in text:
        letter = letter.upper()
        if letter in morse_code:
            converted.append(morse_code[letter])
    return " ".join(converted)

print(converter_to_morse_code("I love dogs and cats"))

reverse_morse = {code: letter for letter, code in morse_code.items()}
def converter_to_reverse_code(morse_text):
    converted_from_morse = []
    for code in morse_text.split(" "):
        if code in reverse_morse:
            converted_from_morse.append(reverse_morse[code])
    return "".join(converted_from_morse)

print(converter_to_reverse_code(".. / .-.. --- ...- . / -.. --- --. ... / .- -. -.. / -.-. .- - ..."))


# Exercise 3 : Box of stars

# Instructions

# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:

def box_printer(*words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)

    print("*" * (longest + 4))

    for word in words:
        spaces = " " * (longest - len(word))
        print("* " + word + spaces + " *")

    print("*" * (longest + 4))


box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

# Exercise 4 : What is the purpose of this code?

# Analyse this code before executing it. What is the purpose of this code?

def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)