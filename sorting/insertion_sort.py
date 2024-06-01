def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


size = int(input("Enter size: "))
list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

print(list1)
insertion_sort(list1)
print(list1)