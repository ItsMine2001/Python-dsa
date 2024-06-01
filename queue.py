class Queue:
    def __init__(self,MS):   # O(n)
        self.arr = [None]*MS
        self.MS = MS
        self.Rear = self.Front = -self.MS-1

    def isEmpty(self):       # O(1)
        return self.Front == -self.MS-1

    def isFull(self):        # O(1)
        return self.Rear == self.MS - 1

    def dequeue(self):       # O(1)
        if self.isEmpty():
            return("Queue is Empty, dequeuing not possible")
        if self.Front == self.Rear:
            data = self.arr[self.Front]
            self.Rear = self.Front = -self.MS-1
        else:
            data = self.arr[self.Front]
            self.Front += 1
        return ("Dequeueing " + str(data))

    def enqueue(self,data):  # O(1)
        if self.isFull():
            print("Queue is Full, enqueuing not possible")
            return
        if self.isEmpty():
            self.Rear = self.Front = 0
            self.arr[self.Rear] = data
        else:
            self.Rear += 1
            self.arr[self.Rear] = data

    def __str__(self):       # O(n)
        items = ""
        if self.isEmpty():
            return items
        for i in range(self.Front, self.Rear+1):
            items = items + str(self.arr[i]) + " "
        return ("Queue Items are: " + items)

    def __len__(self):      # O(1)
        return (self.Rear - self.Front + 1)
        
q = Queue(5)
q.enqueue(11); print(q)
q.enqueue(22); print(q)
q.enqueue(33); print(q)
q.enqueue(44); print(q)
q.enqueue(55); print(q)
q.enqueue(66); print(q)
print(q.dequeue());   print(q)
print(q.dequeue());   print(q)
print(q.dequeue());   print(q)
print(q.dequeue());   print(q)
print(q.dequeue());   print(q)
print(q.dequeue());   print(q)
print(q.dequeue());   print(q)
print(q.dequeue());   print(q)
