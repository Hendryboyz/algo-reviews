class BiNode:
  def __init__(self, value):
    self.value = value
    self.previous = None
    self.next = None
  
class DoublyLinkedList:
  def __init__(self, value):
    self.head = BiNode(value)
    self.tail = self.head
    self.__length = 1
    
  @property
  def length(self):
    return self.__length
  
  def append(self, value):
    new_node = BiNode(value)
    new_node.previous = self.tail
    self.tail.next = new_node
    self.tail = new_node
    self.__length += 1
  
  def prepend(self, value):
    new_node = BiNode(value)
    new_node.next = self.head
    self.head.previous = new_node
    self.head = new_node
    self.__length += 1
  
  def insert(self, index, value):
    if index == 0:
      self.prepend(value)
    elif index >= (self.__length - 1):
      self.append(value)
    else:
      new_node = BiNode(value)
      lead_node = self.__find_leader_node(index)
      next_node = lead_node.next

      new_node.previous = lead_node
      new_node.next = next_node
      lead_node.next = new_node
      next_node.previous = new_node
      self.__length += 1
  
  def __find_leader_node(self, index):
    lead = self.head
    for i in range(index - 1):
      if lead is not None:
        lead = lead.next
    return lead
  
  def remove(self, index):
    if index == 0:
      second = self.head.next
      second.previous = None
      self.head.next = None
      self.head = second
    else:
      lead_node = self.__find_leader_node(index)
      removing_node = lead_node.next
      removing_node.previous = None
      lead_node.next = removing_node.next
      removing_node.next = None
      if lead_node.next == None:
        self.tail = lead_node
      else:
        next_node = lead_node.next
        next_node.previous = lead_node
    self.__length -= 1

  def print_from_begin(self):
    result = []
    current = self.head
    while current is not None:
      result.append(current.value)
      current = current.next
    print(result)

  def print_from_end(self):
    result = []
    current = self.tail
    while current is not None:
      result.append(current.value)
      current = current.previous
    print(result)
