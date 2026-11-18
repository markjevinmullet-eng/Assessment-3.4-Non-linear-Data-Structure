class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class PreOrderTraversal:

  def __init__(self, root_value):
    self.root = Node(root_value)

  def dfs_preorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      result.append(node.value)
      self.dfs_preorder(node.left, result)
      self.dfs_preorder(node.right, result)
    return result


if __name__ == "__main__":
  # Constructing the Binary Tree using First & Last Name: MARK MULLET
  tree = PreOrderTraversal("M")
  tree.root.left = Node("A")
  tree.root.right = Node("R")

  tree.root.left.left = Node("E")
  tree.root.left.right = Node("K")

  tree.root.right.left = Node("L")
  tree.root.right.right = Node("U")

  tree.root.right.left.left = Node("T")

  print("=== PRE-ORDER TRAVERSAL (MARK MULLET) ===")
  print(
      "Pre-Order (Root -> Left -> Right):",
      " -> ".join(tree.dfs_preorder(tree.root)),
  )