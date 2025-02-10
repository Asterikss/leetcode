from collections import deque
from typing import Optional, List


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  # O(n), O(n)
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # type: ignore
    if not root:
      return []

    ret = [[root.val]]
    tmp = []
    q = deque([root, None])
    while q:
      curr_node = q.popleft()  # .pop(0)
      if curr_node is None:
        if not tmp:
          return ret
        q.append(None)
        ret.append(tmp)
        tmp = []
        continue

      if curr_node.left:
        q.append(curr_node.left)
        tmp.append(curr_node.left.val)
      if curr_node.right:
        q.append(curr_node.right)
        tmp.append(curr_node.right.val)

  # Another approach
  def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    q = deque()
    q.append(root)

    while q:
      q_len = len(q)
      level = []
      for _ in range(q_len):
        node = q.popleft()
        if node:
          level.append(node.val)
          q.append(node.left)
          q.append(node.right)
      if level:
        res.append(level)

    return res
