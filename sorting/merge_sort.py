def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    # Merge elements from left and right halves
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Append remaining elements from left half
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1
    
    # Append remaining elements from right half
    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1
    
    return result

size = int(input("Enter Size: "))

list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

print(list1)
merge_sort(list1)
print(list1)

