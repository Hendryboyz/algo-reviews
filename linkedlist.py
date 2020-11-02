class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self, value):
        self.head = node(10)
        self.tail = self.head
        self.__length = 1
    
    @property
    def length(self):
        return self.__length
    
    def append(self, value):
        new_node = node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.__length += 1
    
    def prepend(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node
        self.__length += 1
    
    def traverse(self):
        element = []
        cur = self.head
        while (cur != None):
            element.append(cur.value)
            cur = cur.next
        return element

