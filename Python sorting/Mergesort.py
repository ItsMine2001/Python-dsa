def merge(A, B):
    c = []
    m = len(A)
    n = len(B)
    i, j = 0, 0  
    while i + j < m + n:
        if i == m:
            c.append(B[j])  
            j += 1
        elif j == n:
            c.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    return c  

def mergesort(ll):
    n = len(ll)
    if n <= 1:
        return ll
    L = mergesort(ll[:n // 2])
    R = mergesort(ll[n // 2:])
    ll2 = merge(L, R)
    return ll2

input_arr = [9, 4, 6, 2, 8, 1, 5, 3, 7]
sorted_arr = mergesort(input_arr)
print("Sorted array:",sorted_arr)
