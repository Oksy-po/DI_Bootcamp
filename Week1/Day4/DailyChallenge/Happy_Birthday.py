# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
# Bonus : If they were born on a leap year, display two cakes !

birth_date = input("Give me please your birth date in following format DD/MM/YYYY: ")
day, month, year = birth_date.split("/")
day = int(day)
month = int(month)
year = int(year)
current_year = 2026
age = current_year - year
candles = age % 10
candle_row = "i" * candles
print("   ___" + candle_row + "___")
print("  |:H:a:p:p:y:|")
print("__|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")
# Bonus: second cake if leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("\nYou were born on a leap year! Here's a second cake:\n")
    print("   ___" + candle_row + "___")
    print("  |:H:a:p:p:y:|")
    print("__|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")

