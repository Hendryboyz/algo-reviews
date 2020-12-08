from datastructure.tree import BinaryTreeNode

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
      if value > current.value:
        if current.right == None:
          break
        else:
          current = current.right
      elif value < current.value:
        if current.left == None:
          break
        else:
          current = current.left
      else:
        break

    return path
  
  def __try_balance_tree(self, path):
    sub_tree_root = path.pop()
    parent = path.pop() if len(path) > 0 else None
    while sub_tree_root != None:
      balance_factor = self.__get_balance_factor(sub_tree_root)
      is_balance = abs(balance_factor) <= 1

      if sub_tree_root != None and is_balance == False:
        self.__rotation(parent, sub_tree_root, balance_factor)

      sub_tree_root = parent
      parent = path.pop() if len(path) > 0 else None

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
      self.root = left_node
    else:
      self.__replace_child(parent, current, left_node)
    
  def __replace_child(self, parent, child: BinaryTreeNode, new_child: BinaryTreeNode):
    if parent.left != None and child.value == parent.left.value:
      parent.left = new_child
    else:
      parent.right = new_child

  def remove(self, value):
    path = self.__find_operation_path(value)
    current = path.pop()
    parent = path[-1] if len(path) > 0 else None

    if current == None or current.value != value:
      return False

    if self.__child_count(current) == 0: # is leaf
      self.__replace_child(parent, current, None)
    elif self.__child_count(current) == 1: # only one child
      child = current.left if current.right == None else current.right
      self.__replace_child(parent, current, child)
      path.append(child)
    else:
      successor = self.__find_successor(current)
      successor.left = current.left
      successor.right = current.right
      if parent == None:
        self.root = successor
      else:
        self.__replace_child(parent, current, successor)
      path.append(successor)
    self.__try_balance_tree(path)

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
    while self.__child_count(successor) != 0 and successor.left != None:
      successor_parent = successor
      successor = successor.left

    if successor_parent.left != None and successor.value == successor_parent.left.value:
      successor_parent.left = None
    else:
      successor_parent.right = None

    return successor
