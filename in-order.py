class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class InOrderTraversal:

  def __init__(self, root_value):
    self.root = Node(root_value)

  def dfs_inorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      self.dfs_inorder(node.left, result)
      result.append(node.value)
      self.dfs_inorder(node.right, result)
    return result


if __name__ == "__main__":
  # Constructing the Binary Tree using First & Last Name: MARK MULLET
  tree = InOrderTraversal("M")
  tree.root.left = Node("A")
  tree.root.right = Node("R")

  tree.root.left.left = Node("E")
  tree.root.left.right = Node("K")

  tree.root.right.left = Node("L")
  tree.root.right.right = Node("U")

  tree.root.right.left.left = Node("T")

  print("=== IN-ORDER TRAVERSAL (MARK MULLET) ===")
  print(
      "In-Order (Left -> Root -> Right):",
      " -> ".join(tree.dfs_inorder(tree.root)),
  )