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
      path = self.__find_insertion_path(value)
      parent_node = path[-1]
      if value >= parent_node.value:
        parent_node.right = new_node
      else:
        parent_node.left = new_node
      
      if self.__is_balance(path[2]) == False:
        self.__rotation(path[1], path[2])
      if path[1] != None and self.__is_balance(path[1]) == False:
        self.__rotation(path[0], path[1])
    
  def __find_insertion_path(self, value):
    path = [None] * 3
    current = self.root
    while True:
      path[0] = path[1]
      path[1] = path[2]
      path[2] = current
      if value >= current.value:
        if current.right == None:
          break
        else:
          current = current.right
      else:
        if current.left == None:
          break
        else:
          current = current.left

    return path
  
  def __is_balance(self, node: BinaryTreeNode):
    return abs(self.__get_tree_height(node.left) - self.__get_tree_height(node.right)) <= 1

  def __get_tree_height(self, root: BinaryTreeNode) -> int:
    if root == None:
      return -1
    elif root.left == None and root.right == None:
      return 0
    else:
      return max(self.__get_tree_height(root.left), self.__get_tree_height(root.right)) + 1
  
  def __rotation(self, parent: BinaryTreeNode, target: BinaryTreeNode):
    pass

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

tree = AVLTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)