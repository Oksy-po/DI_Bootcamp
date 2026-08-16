human_years = int(input("How many years ago you took your cat and dog? "))
catYears = 15
dogYears = 15
if human_years >= 2:
    catYears += 9
    dogYears += 9
for year in range(3, human_years + 1):
    catYears += 4
    dogYears += 5
print([human_years, catYears, dogYears])