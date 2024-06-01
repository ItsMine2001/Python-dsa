def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)




size = int(input("Enter Size: "))

list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

print(list1)
heap_sort(list1)
print(list1)























"""
heapify(arr, n, i): This function helps to maintain the heap property (either max heap or min heap) in a binary tree. It compares the element at index i with its children and swaps them if necessary to satisfy the heap property.
    
heap_sort(arr): This function sorts the input array using the heap sort algorithm. It first builds a max heap from the input array, then repeatedly extracts the maximum element from the heap and places it at the end of the array until the entire array is sorted.
"""
