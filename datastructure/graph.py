
class Graph:
  def __init__(self):
    self.node_count = 0
    self.adjacent_list = {}
  
  def add_vertex(self, node):
    all_nodes = self.adjacent_list.keys()
    if node in all_nodes:
      return
    else:
      self.adjacent_list[node] = []
      self.node_count += 1

  def add_edge(self, node1, node2):
    all_nodes = self.adjacent_list.keys()
    if node1 in all_nodes and node2 in all_nodes:
      self.adjacent_list[node1].append(node2)
      self.adjacent_list[node2].append(node1)
    else:
      raise ValueError()

  def show_connections(self):
    all_nodes = self.adjacent_list.keys()
    for node in all_nodes:
      connections = self.adjacent_list[node]
      seperator = ' '
      vertex = seperator.join(connections)
      print(f'{node} --> {vertex}')

class WeightedGraph:
  def __init__(self):
    self.node_count = 0
    self.adjacent_list = {}
  
  def add_vertex(self, node):
    all_nodes = self.adjacent_list.keys()
    if node in all_nodes:
      return
    else:
      self.adjacent_list[node] = []
      self.node_count += 1

  def add_edge(self, node1, node2, weight = 1):
    all_nodes = self.adjacent_list.keys()
    if node1 in all_nodes and node2 in all_nodes:
      self.adjacent_list[node1].append((node2, weight))
      self.adjacent_list[node2].append((node1, weight))
    else:
      raise ValueError()

  def show_connections(self):
    all_nodes = self.adjacent_list.keys()
    for node in all_nodes:
      connections = self.adjacent_list[node]
      print(f'{node} --> {connections}')
