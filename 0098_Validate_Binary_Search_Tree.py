from collections import deque


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  # This took a long time. isValidBST2 is the first version without the
  # helper function. For some reason "child bigger/smaller than the parent
  # of the current node" case did not work and so I ended up maintaining a
  # min and max value throughout the call, for each new node added to the
  # queue, instead of using the parent for comparison. But this seems to work,
  # and that is how it is implemented in solution number 3.
  def isValidBST1(self, root: TreeNode) -> bool:
    def check(curr_node, new_node_val, prev_min, prev_max):
      if prev_min != float("inf"):
        if curr_node.val < prev_min and curr_node.val < prev_max:
          if not new_node_val < prev_min:
            return False
        elif curr_node.val > prev_min and curr_node.val > prev_max:
          if not new_node_val > prev_max:
            return False
        elif (not new_node_val > prev_min) or (
          not new_node_val < prev_max
        ):  # Two cases merged
          return False
      return True

    q = deque([(root, float("inf"), float("-inf"))])  # current, prev_min, prev_max
    while q:
      curr_node, prev_min, prev_max = q.popleft()
      if curr_node.left:
        if curr_node.val <= curr_node.left.val:
          return False
        if not check(curr_node, curr_node.left.val, prev_min, prev_max):
          return False
        q.append(
          (curr_node.left, min(curr_node.val, prev_min), max(curr_node.val, prev_max))
        )
      if curr_node.right:
        if curr_node.val >= curr_node.right.val:
          return False
        if not check(curr_node, curr_node.right.val, prev_min, prev_max):
          return False
        q.append(
          (curr_node.right, min(curr_node.val, prev_min), max(curr_node.val, prev_max))
        )

    return True

  # This took me so long
  def isValidBST2(self, root: TreeNode) -> bool:
    q = deque([(root, float("inf"), float("-inf"))])  # current, prev_min, prev_max
    while q:
      curr_node, prev_min, prev_max = q.popleft()
      if curr_node.left:
        if curr_node.val <= curr_node.left.val:
          return False
        if prev_min != float("inf"):
          if curr_node.val < prev_min and curr_node.val < prev_max:
            if not curr_node.left.val < prev_min:
              return False
          elif curr_node.val > prev_min and curr_node.val > prev_max:
            if not curr_node.left.val > prev_max:
              return False
          elif (not curr_node.left.val > prev_min) or (
            not curr_node.left.val < prev_max
          ):  # Two cases merged
            return False
        q.append(
          (curr_node.left, min(curr_node.val, prev_min), max(curr_node.val, prev_max))
        )
      if curr_node.right:
        if curr_node.val >= curr_node.right.val:
          return False
        if prev_min != float("inf"):
          if curr_node.val < prev_min and curr_node.val < prev_max:
            if not curr_node.right.val < prev_min:
              return False
          elif curr_node.val > prev_min and curr_node.val > prev_max:
            if not curr_node.right.val > prev_max:
              return False
          elif (not curr_node.right.val > prev_min) or (
            not curr_node.right.val < prev_max
          ):  # Two cases merged
            return False
        q.append(
          (curr_node.right, min(curr_node.val, prev_min), max(curr_node.val, prev_max))
        )

    return True

  def isValidBST3(self, root: TreeNode) -> bool:
    def valid(node, left, right):
      if not node:
        return True
      if not (node.val < right and node.val > left):
        return False

      return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, float("-inf"), float("inf"))

  # Inorder traversal and check if sorted.
  def isValidBST4(self, root: TreeNode) -> bool:
    def inorder_traversal(root, res):
      if root:
        inorder_traversal(root.left, res)
        res.append(root.val)
        inorder_traversal(root.right, res)

    def is_sorted(arr):
      if not arr:
        return False
      for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
          return False
      return True

    res = []
    inorder_traversal(root, res)
    return is_sorted(res)
