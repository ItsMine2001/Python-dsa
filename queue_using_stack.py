class Stack:
    def __init__(self,MS):      # O(n)
        self.Arr = [None]*MS
        self.Top = -1
        self.MS = MS       

    def isEmpty(self):          # O(1)
        return self.Top == -1

    def isFull(self):           # O(1)
        return self.Top == self.MS-1
    
    def Push(self, item):       # O(1)
        self.Top += 1
        self.Arr[self.Top] = item

    def Pop(self):              # O(1)
        elem = self.Arr[self.Top]
        self.Top -= 1
        return(elem)

    def peek(self):             # O(1)
        if self.isEmpty():
            return("Stack is EMPTY")
        else:
            return(self.Arr[self.Top])

    def __len__(self):          # O(1)
        return(self.Top+1)

    def __str__(self):          # O(n)
        datalist = ""
        for i in range(self.Top+1):
            datalist += str(self.Arr[i]) + " "
        return datalist


class Queue:
    def __init__(self,MS):      # O(n)
        self.S1=Stack(MS)
        self.S2=Stack(MS)

    def isEmpty(self):          # O(1)
        return self.S1.isEmpty()

    def isFull(self):           # O(1)
        return self.s1.isFull()

    def enqueue(self,ele):      # O(1)
        if self.S1.isFull():
            print("Queue is Full")
            return
        self.S1.Push(ele)

    def dequeue(self):          # O(n)
        if self.S1.isEmpty():
            return("Queue is Empty")
        for i in range(len(self.S1)):
            ele = self.S1.Pop()
            self.S2.Push(ele)

        element = self.S2.Pop()

        for i in range(len(self.S2)):
            ele = self.S2.Pop()
            self.S1.Push(ele)
        return element

    def __str__(self):          # O(n)
        if self.S1.isEmpty():
            return("Queue is Empty")
        else:
            return ("Queue Items: " + str(self.S1))

    def __len__(self):
        return len(self.S1)     # O(1)


q = Queue(5)
q.enqueue(11); print(q)
q.enqueue(22); print(q)
q.enqueue(33); print(q)
q.enqueue(44); print(q)
q.enqueue(55); print(q)
q.enqueue(66); print(q)

print("Length: ",len(q))

print("Dequeuing: ",q.dequeue());   print(q)
print("Dequeuing: ",q.dequeue());   print(q)
print("Dequeuing: ",q.dequeue());   print(q)
print("Dequeuing: ",q.dequeue());   print(q)
print("Dequeuing: ",q.dequeue());   print(q)
print("Dequeuing: ",q.dequeue());   print(q)
print("Dequeuing: ",q.dequeue());   print(q)

print("Length: ",len(q))
