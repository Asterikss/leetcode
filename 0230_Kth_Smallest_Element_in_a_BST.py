class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  # I could also call the function again only when the child is not None, which
  # would simplify it a little bit
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    counter = 0

    def findKthSmallest(node):
      nonlocal counter
      if not node:
        return

      if (ret := findKthSmallest(node.left)) is not None:
        return ret
      counter += 1
      if counter == k:
        print("HERE", node.val)
        return node.val
      if (ret := findKthSmallest(node.right)) is not None:
        return ret

    return findKthSmallest(root)  # type: ignore

  # Brute-force, sorted, then indexed
  def kthSmallest2(self, root: TreeNode, k: int) -> int:
    sorted_nodes = []

    def findKthSmallest(node, sorted_nodes):
      if not node:
        return
      findKthSmallest(node.left, sorted_nodes)
      sorted_nodes.append(node.val)
      findKthSmallest(node.right, sorted_nodes)

    findKthSmallest(root, sorted_nodes)

    return sorted_nodes[k - 1]

  # Without using recursion
  def kthSmallest3(self, root: TreeNode, k: int) -> int:  # type: ignore
    n = 0
    stack = []
    cur = root

    while cur or stack:
      while cur:
        stack.append(cur)
        cur = cur.left

      cur = stack.pop()
      n += 1
      if n == k:
        return cur.val
      cur = cur.right
