def partition(ll, lb, ub):
    pivot = ll[lb]  
    i = lb
    j = ub
    while i < j:
        while i <= j and ll[i] <= pivot:
            i += 1
        while i <= j and ll[j] >= pivot:
            j -= 1
        if i < j:
            ll[i], ll[j] = ll[j], ll[i]
    ll[lb], ll[j] = ll[j], ll[lb]
    return j

def quicksort(ll, start, end):
    if start >= end:
        return
    p = partition(ll, start, end)
    quicksort(ll, start, p - 1)
    quicksort(ll, p + 1, end)

ll = [77,55,66,33,22,44,11]
quicksort(ll, 0, len(ll)-1)
print(ll)
