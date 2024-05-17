from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p:
            # print(p.val, end=" ")
        # else:
            # print("None", end=" ")
        # if q:
            # print(q.val, end=" ")
        # else:
            # print("None", end=" ")
        # print()
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        # print("l")
        # ret1 = self.isSameTree(p.left, q.left)
        # print("r", p.val, q.val)
        # ret2 = self.isSameTree(p.right, q.right)

        # return ret1 and ret2
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
