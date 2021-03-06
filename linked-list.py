class Node:
	# The Node class takes in data and returns Node.next as None
	# By default.
	def __init__(self, data):
		self.data = data
		self.next = None

		return None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, value):
		self.data = value

	def setNext(self, new_next):
		self.next = new_next

class SingleLinkedList:
	""" Docstring for SingleLinkedList """
	def __init__(self):
		self.head = None

	def is_empty(self):
		"""
		Check is liked list is empty.
		"""
		return self.head == None
	
	def add(self, data):
		new_node = Node(data)
		new_node.setNext(self.head)
		self.head = new_node

	def count(self):
		current = self.head
		count = 0

		while current != None:
			count+=1
			current = current.getNext()

		return count

	def search(self, item):
		current = self.head
		found = False

		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

mylist = SingleLinkedList()
mylist.add("Mwiza")
print (mylist.search("Mwiza"))
