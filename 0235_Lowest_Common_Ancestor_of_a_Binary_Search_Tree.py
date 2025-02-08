class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr_ancestor = root
    while True:
      if curr_ancestor.val == p.val or curr_ancestor.val == q.val:
        return curr_ancestor
      if p.val < curr_ancestor.val and q.val < curr_ancestor.val:
        curr_ancestor = curr_ancestor.left
      elif p.val > curr_ancestor.val and q.val > curr_ancestor.val:
        curr_ancestor = curr_ancestor.right
      else:
        return curr_ancestor

  # One if statement less, but this seems to be actually slower
  def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr_ancestor = root
    while True:
      if p.val < curr_ancestor.val and q.val < curr_ancestor.val:
        curr_ancestor = curr_ancestor.left
      elif p.val > curr_ancestor.val and q.val > curr_ancestor.val:
        curr_ancestor = curr_ancestor.right
      else:
        return curr_ancestor
