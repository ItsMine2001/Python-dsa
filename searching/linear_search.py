def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

size = int(input("Enter size: "))
list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

key = int(input("Enter element for search: "))

print(linear_search(list1,key))


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