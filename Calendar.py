# print the month names
# print the days of the week
# print 1-31 on a line
# print the correct number of days in a month
# add line breaks so the days of the week are shown
# start the first day of the year on a specific day other than S
# handle leap year


# define the list of months
monthNames = [
    "January", "February", "March", "April", "May", "June", "July", "August"
]
monthNames += ["September", "October", "November", "December"]


daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

daysPastSunday = int(
    input("Please enter the number of days January 1 is past sunday: "))

year = int(input("Please enter year: "))
if year % 4 == 0:
  daysInMonth[1] = 29


dayNumber = daysPastSunday


print("-" * 50, end="\n")  #just making neat
print(year)

for i in range(len(monthNames)):
  print(monthNames[i])
  for dayOfWeek in "SMTWTFS":
    print("  " + dayOfWeek, end="")
  print()
  #

  print("   " * (dayNumber % 7), end="")
  for j in range(daysInMonth[i]):
    print(f'{j + 1:3}', end="")  ##
    dayNumber += 1
    if dayNumber % 7 == 0 and j != daysInMonth[i] - 1:
      print()
  print("\n")

