class BinaryTreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    new_node = BinaryTreeNode(value)
    if self.root == None:
      self.root = new_node
    else:
      # root = self.root
      parent_node = self.__loop_find_parent(value)
      if value >= parent_node.value:
        parent_node.right = new_node
      else:
        parent_node.left = new_node
  
  def __loop_find_parent(self, value):
    parent = self.root
    while True:
      if value >= parent.value:
        if parent.right == None:
          break
        else:
          parent = parent.right
      else:
        if parent.left == None:
          break
        else:
          parent = parent.left

    return parent

  def __recursive_find_parent(self, current: BinaryTreeNode, value):
    if value >= current.value:
      if current.right == None:
        return current
      else:
        return self.__recursive_find_parent(current.right, value)
    else:
      if current.left == None:
        return current
      else:
        return self.__recursive_find_parent(current.left, value)

  def lookup(self, value):
    current = self.root
    while (current != None) and (current.value != value):
      if value >= current.value:
        current = current.right
      else:
        current = current.left
    return current

  def remove(self, value):
    parent = None
    current = self.root
    while current != None and current.value != value:
      parent = current
      if value > current.value:
        current = current.right
      else:
        current = current.left
    
    if current == None:
      return False

    if self.__child_count(current) == 0: # is leaf
      if parent.left != None and current.value == parent.left.value:
        parent.left = None
      else:
        parent.right = None
    elif self.__child_count(current) == 1: # only one child
      child = current.left if current.right == None else current.right
      if parent.left != None and current.value == parent.left.value:
        parent.left = child
      else:
        parent.right = child
    else:
      successor = self.__find_successor(current)
      successor.left = current.left
      successor.right = current.right
      if parent.left != None and current.value == parent.left.value:
        parent.left = successor
      else:
        parent.right = successor
    
    current.left = None
    current.right = None

    return True
  
  def __child_count(self, node: BinaryTreeNode):
    child_count = 0
    child_count += 1 if node.left != None else 0
    child_count += 1 if node.right != None else 0
    return child_count
  
  def __find_successor(self, node: BinaryTreeNode) -> BinaryTreeNode:
    # find the node in the right subtree that has the minimum value
    successor_parent = node
    successor = node.right
    while self.__child_count(successor) != 0:
      successor_parent = successor
      if successor.left != None:
        successor = successor.left
      else:
        successor = successor.right

    if successor_parent.left != None and successor.value == successor_parent.left.value:
      successor_parent.left = None
    else:
      successor_parent.right = None

    return successor

  def print(self):
    self.__traverse(self.root)
  
  def __traverse(self, node: BinaryTreeNode):
    if node.left != None:
      self.__traverse(node.left)
    print(node.value)
    if node.right != None:
      self.__traverse(node.right)
