class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class PostOrderTraversal:

  def __init__(self, root_value):
    self.root = Node(root_value)

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
  tree = PostOrderTraversal("M")
  tree.root.left = Node("A")
  tree.root.right = Node("R")

  tree.root.left.left = Node("E")
  tree.root.left.right = Node("K")

  tree.root.right.left = Node("L")
  tree.root.right.right = Node("U")

  tree.root.right.left.left = Node("T")

  print("=== POST-ORDER TRAVERSAL (MARK MULLET) ===")
  print(
      "Post-Order (Left -> Right -> Root):",
      " -> ".join(tree.dfs_postorder(tree.root)),
  )