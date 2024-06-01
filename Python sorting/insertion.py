def Insertion_Sort(l):
    print("\n##INSERION SORT##")
    print("-----------------")
    n=len(l)
    for i in range(n-1):
        j=i+1
        while j>0 and l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
            j-=1
        print("Pass",i,": ",l)

    print("SORTED LIST: ",l)
sample_list = [64,25,12,22,11]
Insertion_Sort(sample_list)

    
    
