def m_bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        print("Pass", i, ": ", arr)
        if not swap:
            break
            

size = int(input("Input: "))
l = []
for i in range(size):
    ele = int(input())
    l.append(ele)


print("Before: "); print(l)

print("After m_bubble_sort(): ")
m_bubble_sort(l); print("Final: ",l)
