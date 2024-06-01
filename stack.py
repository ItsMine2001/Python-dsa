class Stack:
    def __init__(self,MS): #O(n)
        self.Arr = [None]*MS
        self.Top = -1
        self.MS = MS       

    def isEmpty(self):     # O(1)
        return self.Top == -1

    def isFull(self):      # O(1)
        return self.Top == self.MS-1
    
    def push(self, item):  # O(1)
        if self.isFull():
            return("Stack is FULL")
        else:
            self.Top += 1
            self.Arr[self.Top] = item

    def pop(self):         # O(1)
        if self.isEmpty():
            return("Stack is EMPTY")
        else:
            elem = self.Arr[self.Top]
            self.Top -= 1
            return(elem)

    def peek(self):        # O(1)
        if self.isEmpty():
            return("Stack is EMPTY")
        else:
            return(self.Arr[self.Top])

    def __len__(self):     # O(1)
        return(self.Top+1)

    def __str__(self):     # O(1)
        datalist = ""
        for i in range(self.Top+1):
            datalist += str(self.Arr[i]) + " "
        return("Stack Items: " + datalist)


S=Stack(5)
print("Popped Out: ",S.pop())
S.push(1); print(S)
print("Popped Out: ",S.pop())
S.push(2); print(S)
S.push(3); print(S)
S.push(4); print(S)
S.push(5); print(S)

print("Length: ",len(s))
print("Popped Out: ",S.pop())
print("Popped Out: ",S.pop())
print("Popped Out: ",S.pop())
print("Popped Out: ",S.pop())
print("Popped Out: ",S.pop())
print(S)
print("Length: ",len(s))
