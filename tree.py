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
      root = self.root
      parent_node = self.__find_parent(root, value)
      if value >= parent_node.value:
        parent_node.right = new_node
      else:
        parent_node.left = new_node
  
  def __find_parent(self, current: BinaryTreeNode, value):
    if value >= current.value:
      if current.right == None:
        return current
      else:
        return self.__find_parent(current.right, value)
    else:
      if current.left == None:
        return current
      else:
        return self.__find_parent(current.left, value)

  def lookup(self, value):
    current = self.root
    while (current != None) and (current.value != value):
      if value >= current.value:
        current = current.right
      else:
        current = current.left
    return current

  def remove(self, value):
    pass
  
  def print(self):
    self.__traverse(self.root)
  
  def __traverse(self, node: BinaryTreeNode):
    if node.left != None:
      self.__traverse(node.left)
    print(node.value)
    if node.right != None:
      self.__traverse(node.right)
