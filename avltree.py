from tree import BinaryTreeNode
class AVLTree:
  def __init__(self):
    self.root = None

  def lookup(self, value):
    current = self.root
    while current != None and current.value != value:
      current = current.left if value < current.value else current.right
    
    return current
  
  def insert(self, value):
    new_node = BinaryTreeNode(value)
    if self.root == None:
      self.root = new_node
    else:
      parent_node = self.__loop_find_parent(value)
      if value >= parent_node.value:
        parent_node.right = new_node
      else:
        parent_node.left = new_node
    
    print ('Current tree height is ' + str(self.__get_tree_height(self.root)))
    
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
  
  def __get_tree_height(self, root: BinaryTreeNode) -> int:
    if root == None:
      return -1
    elif root.left == None and root.right == None:
      return 0
    else:
      return max(self.__get_tree_height(root.left), self.__get_tree_height(root.right)) + 1
  
  def __left_rotation(self, parent: BinaryTreeNode, current: BinaryTreeNode):
    right_node = current.right
    current.right = right_node.left
    right_node.left = current
    self.__replace_child(parent, current, right_node)

  def __right_rotation(self, parent: BinaryTreeNode, current: BinaryTreeNode):
    left_node = current.left
    current.left = left_node.right
    left_node.right = current
    self.__replace_child(parent, current, left_node)
    
  def __replace_child(self, parent, child: BinaryTreeNode, new_child: BinaryTreeNode):
    if parent.left != None and child.value == parent.left.value:
      parent.left = new_child
    else:
      parent.right = new_child
