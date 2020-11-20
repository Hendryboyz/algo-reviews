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
      path = self.__find_operation_path(value)
      parent_node = path[-1]
      if value >= parent_node.value:
        parent_node.right = new_node
      else:
        parent_node.left = new_node
      
      self.__try_balance_tree(path)
      
    
  def __find_operation_path(self, value):
    path = []
    current = self.root
    while True:
      path.append(current)
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
  
  def __try_balance_tree(self, path):
    parent = path.pop()
    ancestor = path.pop() if len(path) > 0 else None
    while parent != None:
      balance_factor = self.__get_balance_factor(parent)
      is_balance = abs(balance_factor) <= 1

      if parent != None and is_balance == False:
        self.__rotation(ancestor, parent, balance_factor)

      parent = ancestor
      ancestor = path.pop() if len(path) > 0 else None

  def __get_balance_factor(self, node: BinaryTreeNode):
    return self.__get_tree_height(node.left) - self.__get_tree_height(node.right)

  def __get_tree_height(self, root: BinaryTreeNode) -> int:
    if root == None:
      return -1
    elif root.left == None and root.right == None:
      return 0
    else:
      return max(self.__get_tree_height(root.left), self.__get_tree_height(root.right)) + 1
  
  def __rotation(self, parent: BinaryTreeNode, target: BinaryTreeNode, balance_factor: int):
    if balance_factor > 1:
      if target.left != None and target.left.left != None: # LL
        self.__right_rotation(parent, target)
      elif target.left != None and target.left.right != None: # LR
        self.__left_rotation(target, target.left)
        self.__right_rotation(parent, target)
    elif balance_factor < -1:
      if target.right != None and target.right.right != None: # RR
        self.__left_rotation(parent, target)
      elif target.right != None and target.right.left != None: # RL
        self.__right_rotation(target, target.right)
        self.__left_rotation(parent, target)
    else:
      return

  def __left_rotation(self, parent: BinaryTreeNode, current: BinaryTreeNode):
    right_node = current.right
    current.right = right_node.left
    right_node.left = current
    if parent == None:
      self.root = right_node
    else:
      self.__replace_child(parent, current, right_node)

  def __right_rotation(self, parent: BinaryTreeNode, current: BinaryTreeNode):
    left_node = current.left
    current.left = left_node.right
    left_node.right = current
    if parent == None:
      self.root == left_node
    else:
      self.__replace_child(parent, current, left_node)
    
  def __replace_child(self, parent, child: BinaryTreeNode, new_child: BinaryTreeNode):
    if parent.left != None and child.value == parent.left.value:
      parent.left = new_child
    else:
      parent.right = new_child
