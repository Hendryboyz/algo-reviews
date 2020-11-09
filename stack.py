from linkedlist import linkedlist

class StackMeta(type):
  def __instancecheck__(cls, instance):
    return cls.__subclasscheck__(type(instance))
  def __subclasscheck__(cls, subclass):
    return (hasattr(subclass, 'push') and callable(subclass.push) and
            hasattr(subclass, 'pop') and callable(subclass.pop) and
            hasattr(subclass, 'peak') and callable(subclass.peak))

class Stack(metaclass=StackMeta):
  pass

class LinkedListStack(Stack):
  def __init__(self):
    self.data = linkedlist()
  
  @property
  def length(self):
    return self.data.length

  def push(self, value):
    self.data.prepend(value)

  def pop(self):
    return self.data.remove(0)

  def peak(self):
    return self.data.head.value
  
  def is_empty(self):
    return self.data.length == 0

class ArrayStack(Stack):
  def push(self, value):
    pass
  def pop(self):
    pass
  def peak(self):
    pass
