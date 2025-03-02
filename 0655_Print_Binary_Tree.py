from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# Just the normal printing of all the levels on by one. I don't care about the
# full problem
class Solution:
  def printTree(self, root: Optional[TreeNode]):
    q = [root, "#"]

    while True:
      for cell in q:
        if cell == "#":
          break
        if cell.left:
          q.append(cell.left)
        if cell.right:
          q.append(cell.right)
      current = q.pop(0)
      if current == "#":
        break
      while current != "#":
        print(current.val, end=" ")
        current = q.pop(0)
      print()
      q.append("#")
