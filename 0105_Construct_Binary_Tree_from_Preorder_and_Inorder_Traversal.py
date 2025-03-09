from typing import List, Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
      return None

    root = TreeNode(preorder[0])
    new_mid = inorder.index(preorder[0])  # leftTreeLength
    root.left = self.buildTree(preorder[1 : new_mid + 1], inorder[:new_mid])
    root.right = self.buildTree(preorder[new_mid + 1 :], inorder[new_mid + 1 :])

    return root

  # Faster, easier to interpret
  def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # takes the left and right bound of inorder, logic --> any given inorder index bisects the tree in left and right subtree
    def localBuildTree(leftBound, rightBound):
      nonlocal preOrderListIndex

      if leftBound > rightBound:
        return None

      newRootVal = preorder[preOrderListIndex]
      newRoot = TreeNode(newRootVal)

      preOrderListIndex += 1

      newRoot.left = localBuildTree(leftBound, inorderIndexFor[newRootVal] - 1)
      newRoot.right = localBuildTree(inorderIndexFor[newRootVal] + 1, rightBound)

      return newRoot

    inorderIndexFor = dict()
    for index, element in enumerate(inorder):
      inorderIndexFor[element] = index

    preOrderListIndex = 0

    return localBuildTree(0, len(preorder) - 1)
