def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


size = int(input("Enter size: "))

list1 = []

for i in range(size):       # it will start with 0 to size-1
    ele = int(input())
    list1.append(ele)

print(list1)
bubble_sort(list1)
print(list1)



'''
OUTPUT: Enter size: 4
        1
        3
        2
        5
        [1, 3, 2, 5]
        [1, 2, 3, 5]
'''