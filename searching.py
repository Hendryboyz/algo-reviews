from datastructure.avltree import AVLTree
from collections import deque

class TreeSearching:
  def __init__(self, nums):
    self.tree = AVLTree()
    for num in nums:
      self.tree.insert(num)
  
  def breadth_first_search(self):
    searching_result = []
    
    upcoming_nodes = deque()
    upcoming_nodes.append(self.tree.root)
    while len(upcoming_nodes) > 0:
      current = upcoming_nodes.popleft()
      searching_result.append(current.value)
      if current.left != None:
        upcoming_nodes.append(current.left)
      if current.right != None:
        upcoming_nodes.append(current.right)
    
    return searching_result
  
  def depth_first_search(self):
    searching_result = []
    
    upcoming_nodes = [ self.tree.root ]
    while len(upcoming_nodes) > 0:
      current = upcoming_nodes.pop()
      searching_result.append(current.value)
      if current.right != None:
        upcoming_nodes.append(current.right)
      if current.left != None:
        upcoming_nodes.append(current.left)

    return searching_result 
