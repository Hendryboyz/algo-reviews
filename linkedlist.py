class node:
  def __init__(self, value):
    self.value = value
    self.next = None

class linkedlist:
  def __init__(self, value = None):
    if value != None:
      self.__init_new_list(value)
    else:
      self.head = None
      self.tail = None
    self.__length = 1 if self.head != None else 0

  def __init_new_list(self, value):
    self.head = node(value)
    self.tail = self.head
  
  @property
  def length(self):
    return self.__length
  
  def append(self, value):
    if self.head == None:
      self.__init_new_list(value)
    else:
      new_node = node(value)
      self.tail.next = new_node
      self.tail = new_node
    self.__length += 1
  
  def prepend(self, value):
    if self.head == None:
      self.__init_new_list(value)
    else:
      new_node = node(value)
      new_node.next = self.head
      self.head = new_node
    self.__length += 1

  def insert(self, index, value):
    if index == 0:
      self.prepend(value)
    elif index >= self.__length:
      self.append(value)
    else:
      new_node = node(value)
      prev = self.__find_leader_node(index)
      new_node.next = prev.next
      prev.next = new_node
      self.__length += 1

  def __find_leader_node(self, index):
    prev = self.head
    for i in range(index - 1):
      if prev.next != None:
        prev = prev.next
    return prev
  
  def remove(self, index):
    if self.__length == 0:
      return
    value = self.head.value
    if index == 0:
      self.head = self.head.next
    else:
      prev = self.__find_leader_node(index)
      value = prev.next.value
      prev.next = prev.next.next
      is_last = (index == self.__length - 1)
      if is_last:
        self.tail = prev
    self.__length -= 1
    return value
  
  def reverse(self):
    if self.__length == 1:
      return
    new_head = self.head
    cur = new_head.next
    self.tail = new_head
    self.head.next = None
    while cur != None:
      cur_next = cur.next
      cur.next = new_head
      new_head = cur
      cur = cur_next
    self.head = new_head

  def print_list(self):
    elements = []
    cur = self.head
    while (cur != None):
      elements.append(cur.value)
      cur = cur.next
    print(elements)
