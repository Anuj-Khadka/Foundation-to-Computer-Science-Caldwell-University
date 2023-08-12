list = [3, 12, 8, 13, 2, 5, 7]
target = 10

for i in range(len(list) - 1):
  for j in range(i+1):
    if list[i] + list[j] == target:
      return i,j
      
