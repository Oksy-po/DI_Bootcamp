# Step 1: Transforming the String into a 2D List
# MATRIX_STR = '''
# 7ir
# Tsi
# h%x
# i ?
# sM# 
# $a 
# #t%''' 
# Step 2: Processing Columns

# Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
# You’ll need to write code that iterates through the columns of your 2D list.
# Think about how you can access the elements of a 2D list by column.      
# temporary_string = ""

MATRIX_STR = """7ir
Tsi
h%x
i ?
sM# 
$a 
#t%"""

# Step 1: split the text into rows
rows = MATRIX_STR.split("\n")

# Step 2: read column by column, collect ALL characters in order
all_characters = ""

for col in range(3):
    for row in rows:
        all_characters += row[col]

# Step 3 & 4: keep only letters, and turn each symbol group into one space
message = ""
skip_space = True   # True = don't add a space right now

for char in all_characters:
    if char.isalpha():
        message += char
        skip_space = False
    elif skip_space == False:
        message += " "
        skip_space = True

# Step 5: print the decoded message
print(message)
