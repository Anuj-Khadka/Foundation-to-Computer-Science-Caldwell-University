from random import randint

def fill(N):
  x = [randint(10, 100) for i in range(N)]
  x.sort()
  return x

a = fill(7)
print(a)

target = int(input("Please enter target"))

low = 0
high = len(a) - 1

while low <= high:
  middle = (low + high) // 2
  if target < a[middle]:
    high = middle - 1
  elif target > a[middle]:
    low = middle + 1
  else:
    print("Found it at position: " + str(middle))
    break

if low > high:
  print("Number is not in the list")
  
