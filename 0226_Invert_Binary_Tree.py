from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        def invertNode(node):            
            if node.left:
                invertNode(node.left)
            if node.right:
                invertNode(node.right)
            tmp = node.left
            node.left = node.right
            node.right = tmp
 
        invertNode(root)
        return root


class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        # or here
        # self.invertTree(root.left)
        # self.invertTree(root.right)
 
        return root
