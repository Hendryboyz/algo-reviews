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
    if is_leaf:
      remove_directly
    elif only_one_child:
      replace_with_child
    else:
      successor = self.__find_successor(current)
      successor.left = current.left
      successor.right = current.right
  
  def __find_successor(self, node: BinaryTreeNode) -> BinaryTreeNode:
    pass

  def print(self):
    self.__traverse(self.root)
  
  def __traverse(self, node: BinaryTreeNode):
    if node.left != None:
      self.__traverse(node.left)
    print(node.value)
    if node.right != None:
      self.__traverse(node.right)
