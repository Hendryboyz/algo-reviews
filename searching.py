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
  
  def breadth_first_search_recursively(self):
    searching_result = []
    
    upcomming_nodes = deque()
    upcomming_nodes.append(self.tree.root)
    self.__execute_bfs_recursively(upcomming_nodes, searching_result)

    return searching_result
  
  def __execute_bfs_recursively(self, nodes, result):
    if len(nodes) == 0:
      return result
    current = nodes.popleft()
    result.append(current.value)
    if current.left != None:
      nodes.append(current.left)
    if current.right != None:
      nodes.append(current.right)
    return self.__execute_bfs_recursively(nodes, result)
  
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
