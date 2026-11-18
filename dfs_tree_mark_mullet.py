class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTreeDFS:

  def __init__(self, root_value):
    self.root = Node(root_value)

  # Pre-Order Traversal (Root -> Left -> Right)
  def dfs_preorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      result.append(node.value)
      self.dfs_preorder(node.left, result)
      self.dfs_preorder(node.right, result)
    return result

  # In-Order Traversal (Left -> Root -> Right)
  def dfs_inorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      self.dfs_inorder(node.left, result)
      result.append(node.value)
      self.dfs_inorder(node.right, result)
    return result

  # Post-Order Traversal (Left -> Right -> Root)
  def dfs_postorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      self.dfs_postorder(node.left, result)
      self.dfs_postorder(node.right, result)
      result.append(node.value)
    return result


if __name__ == "__main__":
  # Constructing the Binary Tree using First & Last Name: MARK MULLET
  # Unique Characters: M, A, R, K, U, L, E, T
  # Tree Structure:
  #         M (Root)
  #       /   \
  #      A     R
  #     / \   / \
  #    E   K L   U
  #         /
  #        T

  tree = BinaryTreeDFS("M")
  tree.root.left = Node("A")
  tree.root.right = Node("R")

  tree.root.left.left = Node("E")
  tree.root.left.right = Node("K")

  tree.root.right.left = Node("L")
  tree.root.right.right = Node("U")

  tree.root.right.left.left = Node("T")

  print("=== ASSESSMENT 3.6: DFS METHOD IN TREE (MARK MULLET) ===")
  print("Pre-Order (Root -> Left -> Right)  :", " -> ".join(tree.dfs_preorder(tree.root)))
  print("In-Order  (Left -> Root -> Right)  :", " -> ".join(tree.dfs_inorder(tree.root)))
  print("Post-Order(Left -> Right -> Root)  :", " -> ".join(tree.dfs_postorder(tree.root)))