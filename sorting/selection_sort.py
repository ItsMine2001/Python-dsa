def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


size = int(input("Enter Size: "))

list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

print(list1)
selection_sort(list1)
print(list1)


'''
OUTPUT: Enter size: 4
        4
        3
        2
        1
        [4, 3, 2, 1]
        [1, 2, 3, 4]
'''