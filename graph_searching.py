import sys

from datastructure.graph import WeightedGraph

class GraphSearching:
  __SHORTEST_DIST_FROM_START = 0
  __PREV_VERTEX = 1
  __DEST_VERTEX = 0
  __EDGE_WEIGHT = 1

  def __init__(self, graph: WeightedGraph, start_vertex = None):
    self.graph = graph
    self.start_vertex = start_vertex
  
  def execute_dijkstra(self):
    if self.start_vertex == None:
      key_list = list(self.graph.adjacent_list.keys())
      self.start_vertex = key_list[0]
    tracking_table = { key: [sys.maxsize, None]  for key in self.graph.adjacent_list.keys() }
    tracking_table[self.start_vertex][0] = 0
    unvisited = list(self.graph.adjacent_list.keys())
    visited = []
    
    current_vertex = self.start_vertex
    while len(unvisited) > 0:
      self.__update_adjacent_vertex_shortest_path(current_vertex, visited, tracking_table)
      
      visited.append(current_vertex)
      unvisited.remove(current_vertex)
      
      current_vertex = self.__decide_next_vertex(tracking_table, unvisited)
    
    self.result_table = tracking_table
    print(f'Starting node is: {self.start_vertex}')
    print(self.result_table)

  def __update_adjacent_vertex_shortest_path(self, current_vertex, visited, tracking_table):
    for edge in self.graph.adjacent_list[current_vertex]:
      dest = edge[self.__DEST_VERTEX]
      if dest in visited:
        continue
      distance = tracking_table[current_vertex][self.__SHORTEST_DIST_FROM_START] + edge[self.__EDGE_WEIGHT]
      has_shorter_path = (distance < tracking_table[dest][self.__SHORTEST_DIST_FROM_START])
      if has_shorter_path:
        tracking_table[dest][self.__SHORTEST_DIST_FROM_START] = distance
        tracking_table[dest][self.__PREV_VERTEX] = current_vertex
    
  def __decide_next_vertex(self, tracking_table, unvisited):
    smallest_cost = sys.maxsize
    next_vertex = None
    for vertex in unvisited:
      if (tracking_table[vertex][self.__SHORTEST_DIST_FROM_START] < smallest_cost):
        smallest_cost = tracking_table[vertex][self.__SHORTEST_DIST_FROM_START]
        next_vertex = vertex

    return next_vertex
  
  def find_path_to(self, vertex):
    current_vertex = self.result_table[vertex]
    shortest_distance = current_vertex[self.__SHORTEST_DIST_FROM_START]
    path = [vertex]
    while current_vertex[self.__PREV_VERTEX] != None:
      path.append(current_vertex[self.__PREV_VERTEX])
      current_vertex = self.result_table[current_vertex[self.__PREV_VERTEX]]
    path.reverse()
    display_path = ' -> '.join(path)
    print(f'path ({display_path}) with shortest distance: {shortest_distance}')
