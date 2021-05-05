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
			self.__init_list(node)
		else:
			self.insertBefore(self.head, node)
	
	def __init_list(self, node):
		self.head = node
		self.tail = node
		
    def setTail(self, node):
		if self.tail is None:
			self.__init_list(node)
		else:
			self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
		if nodeToInsert is self.head and node is self.head:
			return
		self.__transplant(nodeToInsert)
		nodeToInsert.next = node
		nodeToInsert.prev = node.prev
		if node.prev is None: # insert head
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert
	
	def __transplant(self, node):
		if node.prev is not None or node.next is not None:
			self.remove(node)

    def insertAfter(self, node, nodeToInsert):
		if nodeToInsert is self.tail and node is self.tail:
			return
		self.__transplant(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None: # insert tail
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
		if position == 1:
			self.setHead(nodeToInsert)
			
		node = self.head
		shift = position - 1
		while node is not None and shift > 0:
			node = node.next
			shift -= 1
			
		if node is None:
			self.setTail(nodeToInsert)
		else:
			self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        current = self.head
		while current is not None:
			next_node = current.next
			if current.value == value:
				self.remove(current)
			current = next_node

    def remove(self, node):
		prev_node = node.prev
		next_node = node.next
		if prev_node is None: # remvoe head
			self.head = next_node
		else:
			prev_node.next = next_node
			
		if next_node is None: # remove tail
			self.tail = prev_node
		else:
			next_node.prev = prev_node
		
		node.prev = None
		node.next = None
		
    def containsNodeWithValue(self, value):
		current = self.head
		while current is not None and current.value != value:
			current = current.next
		return True if current is not None else False
