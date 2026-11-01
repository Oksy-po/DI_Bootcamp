# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.
def count_occurence(sentence,character):
    count=0
    for letter in sentence:
        if letter==character:
            count +=1
    print(count)

count_occurence("Programming is cool!","o")
count_occurence("This is a great example","y")