# Make an N-by-N  multiplication table like this one without the colors and lines.  Below is an example for N=5.

# *  1  2  3  4  5
# 1  1  2  3  4  5
# 2  2  4  6  8  10
# 3  3  6  9  12 15
# 4  4  8  12 16 20
# 5  5  10 15 20 25

# take user input
n = int(input("Enter the number of rows: "))

# table row header
print("*", end="\t")
for i in range(1, n + 1):
  print(i, end="\t")
print("\n")

# table columns with multiplication
for i in range(1, n + 1):
  print(i, end="\t")
  for j in range(1, n + 1):
    print(j * i, end="\t")
  print("\n")
