from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Codec:
  # Encodes a tree to a single string.
  def serialize(self, root: Optional[TreeNode]) -> str:
    if not root:
      return ""

    ret = ""

    # This could be made simpler easily
    def get_tree(node):  # preorder
      nonlocal ret
      ret += str(node.val) + ","
      if node.left:
        get_tree(node.left)
      else:
        ret += "N,"
      if node.right:
        get_tree(node.right)
      else:
        ret += "N,"

    get_tree(root)
    return ret[:-1]

  # Decodes your encoded data to tree.
  def deserialize(self, data: str) -> Optional[TreeNode]:  # type: ignore
    if not data:
      return None
    data: list[str] = data.split(",")

    root = TreeNode(data[0])  # type: ignore

    # 12NN34NN5NN
    # 12NN34NN5NN
    #   1
    #  2 3
    # N N 4 5
    # 1N[3]46NN7N(N)5NN
    # 1N3[4]6NN7N(N)5NN
    # 1N34[6]N(N)7NN5NN
    #        1
    #       / \
    #      /   \
    #     /     \
    #    /       \
    #   /         \
    #  /           \
    # N             3
    #              / \
    #             /   \
    #            /     \
    #           4       5
    #          / \
    #         6   7
    # 3,2,4,6
    # [3],(2),6,N,N,N,4,N,N F
    # 3,[2],(6),N,N,N,4,N,N F
    # 3,2,[6],(N),N,N,4,N,N 5
    # 3,2,3,N,N,N,4,N,N
    #          3
    #         / \
    #        /   \
    #       /     \
    #      2       4
    #     / \
    #    3   N
    def generate_tree(curr_node, curr_index):
      left_val = data[curr_index]
      last_used_index = -1
      if left_val != "N":
        curr_node.left = TreeNode(left_val)
        last_used_index = generate_tree(curr_node.left, curr_index + 1)

      # if last_used_index == -1:
      #     curr_index = curr_index + 1
      # else:
      #     curr_index = last_used_index + 1
      curr_index = max(last_used_index + 1, curr_index + 1)  # a bit cleaner

      right_val = data[curr_index]
      second_last_used_index = -1
      if right_val != "N":
        curr_node.right = TreeNode(right_val)  # type: ignore
        second_last_used_index = generate_tree(curr_node.right, curr_index + 1)

      # if second_last_used_index != -1:
      #    return second_last_used_index
      # return curr_index
      return max(
        curr_index, second_last_used_index
      )  # The max approach is a bit cleaner

    generate_tree(root, 1)

    return root
