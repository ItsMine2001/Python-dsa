"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)



size = int(input("Enter Size: "))

list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

print(list1)
quick_sort(list1)
print(list1)
"""


def partion(ll,lb,up):
    pivot=ll[lb]
    i=lb
    j=up
    while i<j:
        while i<=j and ll[i]<=pivot:
            i=i+1
        while i<=j and ll[j]>=pivot:
            j=j-1
        if i<j:
            ll[i],ll[j]=ll[j],ll[i]
    ll[lb],ll[j]=ll[j],ll[lb]
    return(j)

def quick_sort(ll,start,end):
    if start>=end:
        return
    p=partion(ll,start,end)
    quick_sort(ll,start,p-1)
    quick_sort(ll,p+1,end)


size = int(input("Enter Size: "))

list1 = []

for i in range(size):
    ele = int(input())
    list1.append(ele)

print(list1)
quick_sort(list1, 0, len(list1)-1)
print(list1)