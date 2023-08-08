print(
  "Pattern 6 has an input variable to get the pattern with user defined number. So, when you are trying the earlier patterns, make sure the variable(somewhere between line 80-90) is commented out.\n Also, if you read this. make sure you comment out this as well which is at Line 1. \n\n Each pattern is commented with a multi line comment. Make sure to uncomment the patterns or just comment the ''' with # for simplicity in each pattern respectively."
)
# Write a program using for loops to produce an R by C rectangle, where R and C are provided by the user.  The following are the triangles for different values of R and C.  R is the number of rows and C is the number of columns.
# Rectangle 3 x 6
# ******
# ******
# ******
'''
R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))
for i in range(R):
  for j in range(C):
    print("*", end="")
  print()
'''

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# Write for loops to produce the following shapes of size n, where the user provides n.  The first three shapes below are the shapes produced where n = 6.  For the last shape, the rectangle, the user provides the height and width.
# Pattern 1:
# *
# *
# *
# *
# *
# *
'''
n = 6
for i in range(n):
  print("*")
'''

# Pattern 2:
# ******
'''
n = 6
for i in range(n):
  print("*", end="")
'''

# Pattern 3:
# ******
# ******
# ******
# ******
# ******
# ******
'''
n = 6
for i in range(n):
  print("*" * n)
'''

# Pattern 4:
# \
#  \
#   \
#    \
#     \
#      \
'''
n = 6
for i in range(n):
  print(i * " " + "\\")
'''

# Pattern 5:
#      /
#     /
#    /
#   /
#  /
# /
'''
n = 6
for i in range(n):
  print((n - i) * " " + "/")
'''

# Pattern 6:
# *
# **
# ***
# ****
# *****
# num = int(input("Enter the number: "))
'''
for i in range(1, num + 1):
  print(i * "*")
'''

# Pattern 7:
# *****
# ****
# ***
# **
# *
'''
for i in range(num, 0, -1):
  print(i * "*")
'''

# Pattern 8:
#      *
#     **
#    ***
#   ****
#  *****
# ******
'''
for i in range(1, num + 1):
  print(" " * (num - i) + "*" * i)
'''

# Pattern 9:
# ******
#  *****
#   ****
#    ***
#     **
#      *
'''
for i in range(num, 0, -1):
  print(" " * (num - i) + "*" * i)
'''

# Pattern 10:
# *
# **
# ***
# ****
# *****
# ******
# ******
# *****
# ****
# ***
# **
# *
'''
for i in range(1, 2 * num):
  # print('*' * min(i, (2 * num - i)))
  print('*' * min(i, (2 * num + 1 - i)))
'''

# Pattern 11:
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
'''
for i in range(1, num + 1):
  print(((num - i) * " ") + ((2 * i - 1) * "*"))
'''

# Pattern 12:
#    1
#   123
#  12345
# 1234567
'''
for i in range(1, num + 1):
  print((num - i) * " ", end="")
  for j in range(2 * i - 1):
    print(j + 1, end="")
  print()
'''
