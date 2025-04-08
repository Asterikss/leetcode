class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxPathSum(self, root: TreeNode) -> int:
    max_sum = float("-inf")

    def find_max(node):
      nonlocal max_sum

      left_val = 0  # could just return 0 if node is None
      right_val = 0

      if node.left:
        left_val = find_max(node.left)
      if node.right:
        right_val = find_max(node.right)

      curr_max = max(left_val + node.val, right_val + node.val, node.val)
      max_sum = max(curr_max, max_sum, right_val + left_val + node.val)

      return curr_max

    find_max(root)

    return int(max_sum)
