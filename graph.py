from collections import deque


class Graph:

  def __init__(self):
    self.adjacency_list = {}

  def add_edge(self, u, v):
    if u not in self.adjacency_list:
      self.adjacency_list[u] = []
    if v not in self.adjacency_list:
      self.adjacency_list[v] = []
    # Avoid duplicate connections in adjacency list
    if v not in self.adjacency_list[u]:
      self.adjacency_list[u].append(v)
    if u not in self.adjacency_list[v]:
      self.adjacency_list[v].append(u)

  def bfs(self, start_vertex):
    visited = set([start_vertex])
    queue = deque([start_vertex])
    traversal_order = []

    while queue:
      current = queue.popleft()
      traversal_order.append(current)

      # Maintain consistent traversal order by sorting neighbors
      for neighbor in sorted(self.adjacency_list.get(current, [])):
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)

    return traversal_order

  def dfs(self, start_vertex, visited=None, traversal_order=None):
    if visited is None:
      visited = set()
    if traversal_order is None:
      traversal_order = []

    visited.add(start_vertex)
    traversal_order.append(start_vertex)

    for neighbor in sorted(self.adjacency_list.get(start_vertex, [])):
      if neighbor not in visited:
        self.dfs(neighbor, visited, traversal_order)

    return traversal_order


if __name__ == "__main__":
  # Graph constructed using the letters of your last name: M, U, L, L, E, T
  # Using unique characters/nodes: M, U, L, E, T
  g = Graph()

  # Define connections matching a similar graph flow
  edges = [
      ("M", "U"),
      ("M", "L"),
      ("U", "L"),
      ("U", "E"),
      ("L", "T"),
      ("E", "T"),
  ]

  for u, v in edges:
    g.add_edge(u, v)

  print("=== GRAPH ===")
  for vertex, neighbors in g.adjacency_list.items():
    print(f"{vertex}: {', '.join(neighbors)}")

  start_node = "M"
  print(f"BFS: {' -> '.join(g.bfs(start_node))}")
  print(f"DFS: {' -> '.join(g.dfs(start_node))}")