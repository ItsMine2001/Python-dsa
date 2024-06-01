def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

size = int(input("Enter size: "))
list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

key = int(input("Enter element for search: "))

print(binary_search(list1,key))


'''
OUTPUT: Enter size: 3
        1
        2
        3
        Enter element for search: 3
        2

        Enter size: 3
        1
        4
        2
        Enter element for search: 6
        -1
'''