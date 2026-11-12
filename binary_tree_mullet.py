from collections import deque


class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:

  def __init__(self, root_value):
    self.root = Node(root_value)

  # Breadth-First Search (Level-Order)
  def bfs(self):
    if not self.root:
      return []
    result = []
    queue = deque([self.root])

    while queue:
      current = queue.popleft()
      result.append(current.value)

      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)

    return result

  # Depth-First Search: Pre-Order (Root -> Left -> Right)
  def dfs_preorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      result.append(node.value)
      self.dfs_preorder(node.left, result)
      self.dfs_preorder(node.right, result)
    return result

  # Depth-First Search: In-Order (Left -> Root -> Right)
  def dfs_inorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      self.dfs_inorder(node.left, result)
      result.append(node.value)
      self.dfs_inorder(node.right, result)
    return result

  # Depth-First Search: Post-Order (Left -> Right -> Root)
  def dfs_postorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      self.dfs_postorder(node.left, result)
      self.dfs_postorder(node.right, result)
      result.append(node.value)
    return result


if __name__ == "__main__":
  # Constructing the Binary Tree for Last Name: MULLET
  #         M
  #       /   \
  #      U     L
  #     / \   /
  #    L   E T

  tree = BinaryTree("M")
  tree.root.left = Node("U")
  tree.root.right = Node("L")
  tree.root.left.left = Node("L")
  tree.root.left.right = Node("E")
  tree.root.right.left = Node("T")

  print("=== BINARY TREE TRAVERSALS (MULLET) ===")
  print("BFS (Level-Order) :", " -> ".join(tree.bfs()))
  print("DFS (Pre-Order)   :", " -> ".join(tree.dfs_preorder(tree.root)))
  print("DFS (In-Order)    :", " -> ".join(tree.dfs_inorder(tree.root)))
  print("DFS (Post-Order)  :", " -> ".join(tree.dfs_postorder(tree.root)))