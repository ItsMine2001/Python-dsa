def selection_sort(arr):
    print("\n##SELECTION SORT##")
    print("------------------")
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
        print("Pass", i, ":", arr)

    print("\nSORTED LIST:", arr)
sample_list = [64, 25, 12, 22, 11]
selection_sort(sample_list)
