from random import randint

def fill(N):
  choice = randint(1, 4)
  if choice == 1:
    return [randint(10, 100) for i in range(N)]
  elif choice == 2:
    return [10 + i for i in range(N)]
  elif choice == 3:
    return [10 + i for i in range(N, 0, -1)]
  else:
    return [randint(10, 12) for i in range(N)]


def sort(a):
  step = 1
  for i in range(len(a)):
    anySwaps = False
    # for j in range(len(a) - 1):
    for j in range(len(a) - 1 - i):

      if a[j] > a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]
        anySwaps = True
      print(format(step, "3d"), a)
      step += 1
    print()
    if not anySwaps:
      break

b = fill(5)
print("   ", b)

sort(b)
print("   ", b)


# ----------------------------------------------
# if the loop is not sorted ---> swap elements
# if the loop is half sorted ---> swap few as needed
# if already sorted ---> no swap
# check for swap in inner loop. if yes, break in outer loop
