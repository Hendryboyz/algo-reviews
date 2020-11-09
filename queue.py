from linkedlist import linkedlist

class Queue:
    def __init__(self):
        self.data = linkedlist()
    
    @property
    def length(self):
        return self.data.length

    def enqueue(self, value):
        self.data.append(value)
    
    def dequeue(self):
        return self.data.remove(0)
    
    def peek(self):
        return self.data.head.value
