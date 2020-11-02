class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self, value):
        self.head = node(value)
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

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == self.__length - 1:
            self.append(value)
        else:
            new_node = node(value)
            prev = self.__find_handle_node(index)
            new_node.next = prev.next
            prev.next = new_node
            self.__length += 1

    def __find_handle_node(self, index):
        prev = self.head
        for i in range(index - 1):
            if prev.next != None:
                prev = prev.next
        return prev
    
    # def remove(self, index):
        # todo

    def print_list(self):
        elements = []
        cur = self.head
        while (cur != None):
            elements.append(cur.value)
            cur = cur.next
        print(elements)
