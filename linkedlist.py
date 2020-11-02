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
        self.tail.next = node(value)
        self.tail = self.tail.next
        self.__length += 1
    
    def traverse(self):
        element = []
        cur = self.head
        while (cur != None):
            element.append(cur.value)
            cur = cur.next
        return element

my_linked_list = linkedlist(10)
my_linked_list.append(1)
my_linked_list.append(15)
my_linked_list.traverse()
