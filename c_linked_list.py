class Node:
    def __init__(self,val=None):
        self.data=val
        self.next=self
        
    def isEmpty(self):
        return(self.data==None and self.next==self)

    def append(self,value):
        if self.isEmpty():
            self.data=value
            self.next=self
            return
        temp=self
        while temp.next!=self:
            temp=temp.next
        newnode=Node(value)    
        temp.next=newnode
        newnode.next=self

    def insert_at_begin(self,value):
         if self.isEmpty():
            self.data=value
            self.next=self
            return
         newnode=Node(value)
         self.data,newnode.data=newnode.data,self.data
         newnode.next=self.next
         self.next=newnode

    def insert_after_node(self,value,v):
        if self.isEmpty():
            return("the node is not present")
        temp=self
        while temp.data!=v:
            if temp.next==self:
                return("the node is not present")
            else:
                temp=temp.next
        newnode=Node(value)
        if temp.next!=self:        
             newnode.next=temp.next
             temp.next=newnode
        else:
            temp.next=newnode
            newnode.next=self

    def insert_before_node(self,value,v):
         if self.isEmpty():
            return("the node is not present")
         temp=self
         newnode=Node(value)
         if self.data==v:
           self.insert_at_begin(value)
           return
         while temp.next.data!=v:
             if temp.next.next==self:
                 return("the node is not present")
             else:
                 temp=temp.next
         newnode.next=temp.next
         temp.next=newnode
    
    def insert_at_position(self,value,p):
       if p<0:
           return("invalid position")
       if self.isEmpty():
            return("the list is empty")
       if p==0:
         self.insert_at_begin(value)
         return
       c=1
       temp=self
       while c!=p:
           if temp.next==self:
               return("upto this position the list is not present")
           else:
               temp=temp.next
               c+=1
       newnode=Node(value)        
       if temp.next!=self:        
             newnode.next=temp.next
             temp.next=newnode
       else:
            temp.next=newnode
            newnode.next=self
            
    def delete_1st_node(self):
        if self.data==None:
            return("enpty list")
        if self.next==self:
            self.data=None
            return
        if self.next.next==self:
            self.data=self.next.data
            self.next=self
            return
        self.data=self.next.data
        self.next=self.next.next

    def delete_last_node(self):
        if self.data==None:
            return("enpty list")
        if self.next==self:
            self.data=None
            return
        temp=self
        while temp.next.next!=self:
            temp=temp.next
        temp.next=self

    def delete_specific_node(self,d):
        if self.data==None:
            return("enpty list")
        if self.data==d and self.next==self:
            seld.data=None
            return
        if self.data==d :
            self.delete_1st_node()
            return
        temp=self
        while temp.next.data!=d:
            if temp.next!=self:
                temp=temp.next
            else:
                return
        if temp.next.next==self:
            temp.next=self
        else:
            temp.next=temp.next.next

    def  delete_after_node(self,d):
        if self.data==None or self.next==None:
            return
        temp=self
        while temp.data!=d:
            if temp.next!=self:
                temp=temp.next
            else:
                return
        if temp.next.next!=self:
           temp.next=temp.next.next
        else:
           temp.next=None

    def delete_before_node(self,d):
       if self.data==None or self.next==None:
            return
       if self.next.data==d:
           self.delete_1st_node()
           return
       temp=self
       while temp.next.next.data!=d:
           if temp.next.next!=self:
               temp=temp.next
           else:
               return
       temp.next=temp.next.next

    def delete_position_node(self,p):
        if self.data==self:
            return("empty")
        c=0
        if p==0:
            self.delete_1st_node()
            return
        temp=self
        while c!=p-1:
             if temp.next!=self:
                 temp=temp.next
                 c=c+1
             else:
                 return
        if temp.next.next==self:
            temp.next=self
        else:
            temp.next=temp.next.next

    def __str__(self):
         d=""
         temp=self
         if self.isEmpty():
            return("emprt list")
         while temp.next!=self:
             d=d+ str(temp.data) + " -> "
             temp=temp.next
         d=d+ str(temp.data) + " "
         return(d)

    def __len__(self):
        if self.isEmpty():
            return("the list is empty")
        c=0
        temp=self
        while temp.next!=self:
            temp=temp.next
            c+=1
        c+=1
        return(c)
                


              
print("Append")       
n=Node(10); print(n)

n.append(20); print(n)

n.append(30); print(n)

print("lenght is",len(n))
print()
n.insert_after_node(35,20); print(n)

print("\nlenght is",len(n))

print("\nInsert Befrore Node")
n.insert_before_node(25,30); print(n)
print("\nInsert At Begin")
n.insert_at_begin(50); print(n)
print("\nInsert At Position")
n.insert_at_position(40,0); print(n)
print("\nDelete Last None")
n.delete_last_node(); print(n)
print("\nDelete Before None")
n.delete_before_node(20); print(n)
print("\nDelete Position None")
n.delete_position_node(2); print(n)
print("\nDelete Before None")
n.delete_before_node(50); print(n)


