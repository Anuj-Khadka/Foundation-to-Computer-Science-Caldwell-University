def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


list = [45, 32, 56, 12, 52, 76, 10]
insertion_sort(list)
#print("Sorted list:", list)
for i in range(len(list)):
  print (list[i],end=" ")
