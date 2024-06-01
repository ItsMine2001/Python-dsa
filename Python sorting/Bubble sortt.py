def bubblesort(arr,n):
    print("\n Bubble Sort")
    print(" ")
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[i]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
            print("pan",i,":",arr)
            if not swapped:
                break
        print()
        print("Sorted list",arr)
arr = []
n = int(input("Enter how many elements:"))
for i in range(n):
    val = int(input("Enter the value: "))
    arr.append(val)
bubblesort(arr,n)
