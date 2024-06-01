class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insertAtBegin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		else:
			new_node.next = self.head
			self.head = new_node

	def insertAtIndex(self, data, index):
		new_node = Node(data)
		current_node = self.head
		position = 0
		if position == index:
			self.insertAtBegin(data)
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				new_node.next = current_node.next
				current_node.next = new_node
			else:
				print("Index not present")

	def insertAtEnd(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return

		current_node = self.head
		while(current_node.next):
			current_node = current_node.next

		current_node.next = new_node

	def remove_first_node(self):
		if(self.head == None):
			return

		self.head = self.head.next

	def remove_last_node(self):

		if self.head is None:
			return

		current_node = self.head
		while(current_node.next.next):
			current_node = current_node.next

		current_node.next = None

	def remove_at_index(self, index):
		if self.head == None:
			return

		current_node = self.head
		position = 0
		if position == index:
			self.remove_first_node()
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")

	def remove_specific_node(self, data):
		current_node = self.head

		if current_node.data == data:
			self.remove_first_node()
			return

		while(current_node != None and current_node.next.data != data):
			current_node = current_node.next

		if current_node == None:
			return
		else:
			current_node.next = current_node.next.next

	def remove_after_node(self, data):
		current_node = self.head
		while current_node and current_node.data != data:
			current_node = current_node.next
		if current_node and current_node.next:
			current_node.next = current_node.next.next

	def remove_before_node(self, data):
		current_node = self.head
		if current_node and current_node.data == data:
			return
		while current_node and current_node.next and current_node.next.data != data:
			current_node = current_node.next
		if current_node and current_node.next:
			current_node.next = current_node.next.next

	'''
	# Print the size of linked list
	def sizeOfLL(self):
		size = 0
		if(self.head):
			current_node = self.head
			while(current_node):
				size = size+1
				current_node = current_node.next
			return size
		else:
			return 0

	# print method for the linked list
	def printLL(self):
		current_node = self.head
		while(current_node):
			print(current_node.data)
			current_node = current_node.next
	'''

	def __str__(self):
		result = []
		current_node = self.head
		while current_node:
			result.append(str(current_node.data))
			current_node = current_node.next
		return " -> ".join(result)

	def __len__(self):
		count = 0
		current_node = self.head
		while current_node:
			count += 1
			current_node = current_node.next
		return count



llist = LinkedList()

llist.insertAtEnd(11)
llist.insertAtEnd(22)
llist.insertAtBegin(33)
llist.insertAtEnd(44)
llist.insertAtIndex(55, 2)
llist.insertAtEnd(77)
llist.insertAtEnd(66)
llist.insertAtEnd(88)

print("Node Data")
#llist.printLL()
print(llist)


print("\nRemove First Node")
llist.remove_first_node()
print(llist)
print("Remove Last Node")
llist.remove_last_node()
print(llist)
print("Remove Node at Index 1")
llist.remove_at_index(1)
print(llist)
print("Remove Specific Node value:(44)")
llist.remove_specific_node(44)
print(llist)
print("Remove After a Node value:(11)")
llist.remove_after_node(11)
print(llist)
print("Remove Before a Node value:(66)")
llist.remove_before_node(66)
print(llist)


print("\nLinked list after removing a node:")
#llist.printLL()
print(llist)


print("\nSize of Linked List :", end=" ")
#print(llist.sizeOfLL())
print(len(llist))

