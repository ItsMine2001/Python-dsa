#Implementation of Double Ended Queue
class DEQueue:
    def __init__(self,MS):
        self.arr=[None]*MS
        self.MS=MS
        self.r=self.f=-self.MS-1
    def isEmpty(self):
        return(self.f==-self.MS-1)
    def isFull(self):
        return(self.r+1)%self.MS==self.f
    def rear_enqueue(self,ele):
        if self.isEmpty():
            self.f=self.r=0
            self.arr[self.r]=ele
            print("insert element:",ele)
            return
        if self.isFull():
          print("Queue is full")
          return
        self.r=(self.r+1)%self.MS
        self.arr[self.r]=ele
        print("insert element:",ele)
        return
    def front_dqueue(self):
        if self.isEmpty():
          print("Queue is Empty")
          return
        if self.r==self.f:
            ele=self.arr[self.f]
            self.f=self.r=-self.MS-1
            print("delete element:",ele)

        else:
            ele=self.arr[self.f]
            self.f=(self.f+1)%self.MS
            print("delete element:",ele)
            return
    def front_enqueue(self,ele):
        if self.isFull():
            print("Overflow")
            return
        if self.f==0:
            self.f=self.MS-1
            self.arr[self.f]=ele
            print("insert element:",ele)
            return
        else:
            self.f=self.f-1
            self.arr[self.f]=ele
            print("insert element:",ele)
            return
    def rear_dqueue(self):
        if self.isEmpty():
            print("Underflow")
            return
        if self.r==0:
            ele=self.arr[self.r]
            self.r=self.MS-1

        else:
            ele=self.arr[self.r]
            self.r=self.r-1
        print("delete element:",ele)
        return
    def __str__(self):
        data=""
        if self.isEmpty():
            print("none")
            return(data)
        if self.f<=self.r:
            for i in range(self.f,self.r+1):
                data+=str(self.arr[i])+" "
        else:
            for i in range(self.f,self.MS):
                data+=str(self.arr[i])+" "
            for i in range(self.r+1):
                data+=str(self.arr[i])+" "
        print("Display the Queue:",end="")
        return(data)
    def __len__(self):
        if self.isEmpty():
           return 0
        if self.f<=self.r:
            print("Length of the Queue:",end="")
            return(self.r-self.f+1)
        else:
            print("Length of the Queue:",end="")
            return((self.MS-self.f)+(self.r+1))
n=DEQueue(6)
n.rear_enqueue(1)
n.rear_enqueue(2)
n.rear_enqueue(3)
print(str(n))
n.front_enqueue(4)
print(str(n))
print(len(n))
n.rear_dqueue()
print(str(n))
print(len(n))
n.front_dqueue()
print(str(n))
print(len(n))
n.rear_dqueue()
print(str(n))
print(len(n))
n.front_dqueue()
print(str(n))
print(len(n))

