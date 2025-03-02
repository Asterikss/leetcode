from typing import Deque, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution2:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0

    lvl = 1
    q = Deque([root])
    l = len(q)

    while q:
      if l > 0:
        curr = q.popleft()
        if curr.left:
          q.append(curr.left)
        if curr.right:
          q.append(curr.right)
        l -= 1

      else:
        if len(q) == 0:
          return lvl

        lvl += 1
        l = len(q)

    return lvl

  def maxDepth2(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    level = 0
    q = Deque([root])
    while q:
      for _ in range(len(q)):
        node = q.popleft()
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      level += 1
    return level


class Solution3:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0

    def walk(current, depth, max_depth) -> int:
      if current is None:
        return max_depth

      if depth > max_depth:
        max_depth = depth

      m1 = walk(current.left, depth + 1, max_depth)
      m2 = walk(current.right, depth + 1, max_depth)

      # print(max_depth, m1, m2)
      return max(max_depth, m1, m2)

    return walk(root, 1, 1)


class Solution4:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0
    stack = [(root, 1)]
    maks_depth = 1
    visited = set()
    while stack:
      current = stack[-1][0]
      depth: int = stack[-1][1]
      visited.add(current)
      # print(current.val)
      # print(depth)
      if current.left and current.left not in visited:
        stack.append((current.left, depth + 1))
      elif current.right and current.right not in visited:
        stack.append((current.right, depth + 1))
      else:
        if depth > maks_depth:
          maks_depth = depth
        stack.pop()

    return maks_depth

  def maxDepth2(self, root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]
    res = 0

    while stack:
      node, depth = stack.pop()

      if node:
        res = max(res, depth)
        stack.append([node.left, depth + 1])
        stack.append([node.right, depth + 1])
    return res
