original_sentence="You have entered a wrong domain"
print(original_sentence)
updated_sentence=original_sentence.split(" ")
updated_sentence=list(updated_sentence)
updated_sentence.sort(reverse=True)
print(updated_sentence)

# Perfect number

# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers

x = int(input('Enter the Number:'))
all_divisors=[]

for divisor in range (1, x):
    if x % divisor ==0:
        all_divisors.append(divisor)

if sum(all_divisors) ==x:
    print(True)
else:
    print(False)






