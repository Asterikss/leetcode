from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root and not subRoot:
      return True
    if not root or not subRoot:
      return False

    parts_of_root = []

    if root.val == subRoot.val:
      parts_of_root.append(root)

    q = [root]
    while q:
      current = q.pop(0)
      if current.left:
        if current.left.val == subRoot.val:
          parts_of_root.append(current.left)
        q.append(current.left)
      if current.right:
        if current.right.val == subRoot.val:
          parts_of_root.append(current.right)
        q.append(current.right)

    def is_same(part_of_root):
      q_root = [part_of_root]
      q_subroot = [subRoot]

      while q_root:
        curr_root = q_root.pop(0)
        curr_subroot = q_subroot.pop(0)
        if type(curr_root.left) != type(curr_subroot.left):
          return False
        if type(curr_root.right) != type(curr_subroot.right):
          return False

        if curr_root.left:
          if curr_root.left.val != curr_subroot.left.val:  # type:ignore
            return False
          q_root.append(curr_root.left)
          q_subroot.append(curr_subroot.left)  # type:ignore

        if curr_subroot.right:
          if curr_root.right.val != curr_subroot.right.val:
            return False
          q_root.append(curr_root.right)
          q_subroot.append(curr_subroot.right)

      return True

    for part_of_root in parts_of_root:
      if is_same(part_of_root):
        return True

    return False
