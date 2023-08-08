# Write a program to calcualte the years it takes to double the money when the initial amount, increase rate are given.

amount = float(input("Enter the amount: "))
given_rate = float(input("Enter the rate: "))
years = 0
double_amount = 2 * amount

while amount <= double_amount:
  interest = (amount * given_rate) / 100
  amount += interest
  years += 1
  # print(f'{years} - ${amount}')

print(f'\nThe total time required to double the amount is {years} years.')
