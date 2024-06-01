#Implementation of Doubly LinkList
class Node:
    def __init__(self,val1=None):
        self.prev=None
        self.data=val1
        self.next=None
    def append(self,val1):
        if self.data==None:
            self.data=val1
            return
        temp=self
        while temp.next!=None:
            temp=temp.next
        newNode=Node(val1)
        temp.next=newNode
        newNode.prev=temp
    def insert_at_begin(self,val1):
        if self.data==None:
            self.data=val1
            return
        if self.next==None:
            newNode=Node(val1)
            self.data,newNode.data=newNode.data,self.data
            self.next=newNode
            newNode.prev=self
            return
        newNode=Node(val1)
        self.data,newNode.data=newNode.data,self.data
        newNode.next=self.next
        newNode.next.prev=newNode
        self.next=newNode
        newNode.prev=self

    def insert_after_node(self,val1,val):
        if self.data==None:
            self.data=val1
            return
        temp=self
        while temp!=None:
            if temp.data==val1:
                newNode=Node(val)
                newNode.next=temp.next
                if temp.next!=None:
                   temp.next.prev=newNode
                temp.next=newNode
                newNode.prev=temp
                return newNode
            temp=temp.next

    def insert_before_node(self,val1,val):
        if self.data==None:
            self.data=val1
            return
        if self.data==val1:
            newNode=Node(val)
            newNode.next=self
            self.prev=newNode
            return newNode
        temp=self
        while temp!=None:
            if temp.data==val1:
                newNode=Node(val)
                newNode.prev=temp.prev
                newNode.next=temp
                if temp.prev!=None:
                   temp.prev.next=newNode
                temp.prev=newNode
                return newNode
            temp=temp.next
    
    def insert_at_position(self,val1,val):
        if self.data==None:
            self.data=val1
            return
        c=0
        temp=self
        while c!=val1-1:
            if temp.next==None:
                return
            else:
                temp=temp.next
                c=c+1
        newNode=Node(val)
        newNode.next=temp.next
        if temp.next!=None:
            temp.next.prev=newNode
        temp.next=newNode
        newNode.prev=temp

    def delete_first_node(self):
        if self.data==None:
            return
        if self.next==None:
            self.data=None
            return
        if self.next.next==None:
            self.data,self.next.data=self.next.data,self.data
            self.next=self
            return
        self.data,self.next.data=self.next.data,self.data
        self.next=self.next.next
        self.next.prev=self

    def delete_last_node(self):
        if self.data==None:
            return
        if self.next==None:
            self.data=None
            return
        temp=self
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None

    def delete_specific_node(self,val1):
        if self.data==None:
            return
        if self.next==None and self.data==val1:
            self.data=None
            return
        if self.data==val1:
            self.delete_first_node()
            return
        temp=self
        while temp.next.data!=val1:
            if temp.next!=None:
                temp=temp.next
            else:
                return
        if temp.next.next==None:
            temp.next=None
        else:
            temp.next=temp.next.next
            temp.next.prev=temp

    def delete_after_node(self,val1):
        if self.data==None or self.next==None:
            return
        temp=self
        while temp.data!=val1:
            if temp.next==None:
                return
            else:
                temp=temp.next
        if temp.next==None:
            return
        else:
            temp.next=temp.next.next
            temp.next.prev=temp

    def delete_before_a_node(self, val1):
      if self.data == None or self.next == self:
        return
      if self.next.data == val1:
        self.delete_first_node()
        return
      temp = self
      while temp.next.next.data != val1:
        if temp.next.next == None:
            temp.next = temp.next.next
            return
        else:
            temp = temp.next
      if temp.next == None:
        return
      temp.next = temp.next.next
      temp.next.prev=temp

    def delete_position_node(self,p):
        if self.data==None:
            return
        c=0
        if p==0:
            self.delete_first_node()
            return
        temp=self
        while c!=p-1:
            if temp.next!=None:
                temp=temp.next
                c=c+1
            else:
                return
        if temp.next.next==None:
            temp.next=None
        else:
            temp.next=temp.next.next
            temp.next.prev=temp

    
    def __str__(self):
        datalist=""
        if self.data==None:
            return(datalist)
        datalist+=str(self.data)+" "
        temp=self
        while temp.next!=None:
            temp=temp.next
            datalist+=str(temp.data)+" "
        return(datalist)
    def __len__(self):
       c=0
       temp=self
       while temp!=None:
          c=c+1
          temp=temp.next
       return c
    
    
n=Node()
n.append(10)
print(n)
print("No.of Nodes in the list=",len(n))

n.append(20)
print(n)
print("No.of Nodes in the list=",len(n))
n.insert_at_begin(1)
print(n)
print("No.of Nodes in the list=",len(n))
n.insert_after_node(10,100)
print(str(n))
print("No.of Nodes in the list=",len(n))
n.insert_after_node(100,400)
print(str(n))
print("No.of Nodes in the list=",len(n))

n.insert_before_node(100,800)
print(str(n))
n.insert_at_begin(2)
print(n)
print("No.of Nodes in the list=",len(n))
n.insert_before_node(20,200)
print(str(n))
print("No.of Nodes in the list=",len(n))
n.insert_before_node(1,300)
print(str(n))
print("No.of Nodes in the list=",len(n))
n.insert_at_position(4,500)
print(str(n))
print("No.of Nodes in the list=",len(n))
n.insert_at_position(8,600)
print(str(n))
print("No.of Nodes in the list=",len(n))
n.insert_at_position(1,700)
print(str(n))
print("No.of Nodes in the list=",len(n))

n.delete_first_node()
print(str(n))
print("No.of Nodes in the list=",len(n))

n.delete_last_node()
print(str(n))
print("No.of Nodes in the list=",len(n))

n.delete_specific_node(300)
print(str(n))
print("No.of Nodes in the list=",len(n))

n.delete_after_node(400)
print(str(n))
print("No.of Nodes in the list=",len(n))

n.delete_before_a_node(200)
print(str(n))
print("No.of Nodes in the list=",len(n))

n.delete_position_node(2)
print(str(n))
print("No.of Nodes in the list=",len(n))



            
