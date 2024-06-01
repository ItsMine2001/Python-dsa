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
        if self.next==self:
            newnode=Node(value)
            self.data,newnode.data=newnode.data,self.data
            self.next=newnode
            newnode.next=self
            return
        newnode=Node(value)
        self.data,newnode.data=newnode.data,self.data
        newnode.next=self.next
        self.next=newnode
        
    def insert_after_node(self,value,v):
        if self.isEmpty():
            return("empty list")
        temp=self
        while temp.data!=value:
            if temp.next==self:
                return("empty list")
            else:
                temp=temp.next
        newnode=Node(v)
        if temp.next!=self:        
             newnode.next=temp.next
             temp.next=newnode
        else:
            temp.next=newnode
            newnode.next=self
            
    def insert_before_node(self,value,v):
        if self.isEmpty():
            return("empty list")
        temp=self
        newnode=Node(v)
        if self.data==value:
            self.insert_at_begin(v)
            return
        while temp.next.data!=value:
            if temp.next.next==self:
                return("the node is not present")
            else:
                temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    
    def insert_at_position(self,value,pos):
        if pos<0:
            return("invalid position")
        if self.isEmpty():
            return("the list is empty")
        if pos==0:
            self.insert_at_begin(value)
            return
        c=1
        temp=self
        while c!=pos-1:
            if temp.next==self:
                return("upto this position list is not present")
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
            
    def delete_first_node(self):
        if self.data==None:
            return("empty list")
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

    def delete_specific_node(self,dv):
        if self.data==None:
            return("enpty list")
        if self.data==dv and self.next==self:
            seld.data=None
            return
        if self.data==dv :
            self.delete_1st_node()
            return
        temp=self
        while temp.next.data!=dv:
            if temp.next!=self:
                temp=temp.next
            else:
                return
        if temp.next.next==self:
            temp.next=self
        else:
            temp.next=temp.next.next

    def  delete_after_node(self,dv):
        if self.data==None or self.next==self:
            return
        temp=self
        while temp.data!=dv:
            if temp.next!=self:
                temp=temp.next
            else:
                return
        if temp.next.next!=self:
           temp.next=temp.next.next
        else:
           temp.next=self

    def delete_before_node(self,dv):
        if self.data==None or self.next==self:
            return("not possible")
        if self.next.data==dv:
           self.delete_first_node()
           return
        temp=self
        while temp.next.next.data!=dv:
            if temp.next.next!=self:
                temp=temp.next
                
            else:
                return
        temp.next=temp.next.next

    def delete_position_node(self,pos):
        if self.data==self:
            return("empty list")
        c=0
        if pos==0:
            self.delete_1st_node()
            return
        temp=self
        while c!=pos-1:
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
        data=""
        temp=self
        if self.isEmpty():
            return("empty list")
        while temp.next!=self:
            data=data + str(temp.data) + " "
            temp=temp.next
        data=data + str(temp.data) + " "
        return(data)
         
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
                
              
cll=Node()
print(cll)
cll.append(10)
cll.append(20)
cll.append(30)
print(cll)
print("length of the list:",len(cll))
print("insertion at begning of node")
cll.insert_at_begin(5)
print(cll)
print("insertion after given node")
cll.insert_after_node(10,15)
print(cll)
print("insertion before a given node")
cll.insert_before_node(30,25)
print(cll)
print("insertion at given position")
cll.insert_at_position(50,4)
print(cll)
print("deletion of first node")
cll.delete_first_node()
print(cll)
print("deletion of last node")
cll.delete_last_node()
print(cll)
print("delete specific node")
cll.delete_specific_node(50)
print(cll)
print("deletion after a node")
cll.delete_after_node(15)
print(cll)
print("deletion before a node")
cll.delete_before_node(25)
print(cll)
print("delete position node")
cll.delete_position_node(1)
print(cll)
print("lenght of the list:",len(cll))