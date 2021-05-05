# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
		if self.head is None:
			self.__insert_first_node(node)
		else:
			self.remove(node)
			node.next = self.head
			self.head.prev = node
			self.head = node
	
	def __insert_first_node(self, node):
		self.head = node
		self.tail = node

    def setTail(self, node):
		if self.tail is None:
			self.__insert_first_node(node)
		else:
			self.remove(node)
			node.prev = self.tail
			self.tail.next = node
			self.tail = node

    def insertBefore(self, node, nodeToInsert):
		prev_node = node.prev
		if prev_node is None:
			self.setHead(nodeToInsert)
		else:
			self.remove(nodeToInsert)
			nodeToInsert.prev = prev_node
			nodeToInsert.next = node
			prev_node.next = nodeToInsert
			node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
		next_node = node.next
		if next_node is None:
			self.setTail(nodeToInsert)
		else:
			self.remove(nodeToInsert)
			nodeToInsert.prev = node
			nodeToInsert.next = next_node
			next_node.prev = nodeToInsert
			node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
		if position == 1:
			self.setHead(nodeToInsert)
		else:
			iteration_time = position - 1
			node = self.head
			while iteration_time > 0 and node is not None:
				node = node.next
				iteration_time -= 1
			if node is None:
				self.setTail(nodeToInsert)
			else:
				self.remove(nodeToInsert)
				self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
		cur = self.head
		while cur is not None:
			node = cur if cur.value == value else None
			cur = cur.next
			if node is not None:
				self.remove(node)

    def remove(self, node):
		if node is self.head:
			self.head = node.next 
		if node is self.tail:
			self.tail = node.prev
		self.__clear_node_dependency(node)
	
	def __clear_node_dependency(self, node):
		prev_node = node.prev
		next_node = node.next
		node.prev = node.next = None
		if prev_node is not None:
			prev_node.next = next_node
		if next_node is not None:
			next_node.prev = prev_node

    def containsNodeWithValue(self, value):
		node = self.__find_node_with_value(value)
		return True if node is not None else False
	
	def __find_node_with_value(self, value):
		cur = self.head
		while cur is not None and cur.value != value:
			cur = cur.next
		return cur
