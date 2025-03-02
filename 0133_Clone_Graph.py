from typing import Optional


class Node:
  def __init__(self, val=0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []


class Solution:
  # Legendary solution
  def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
    if not node:
      return

    res = []
    visited = set()

    # [[2],[1,3],[2]]
    # [[2], [1,3]]
    # stack [node3]
    # --
    # [[2,3],[1,4],[1,4],[2,3]]
    # res [[2, 3], [1, 4], [1,4], [2, 3]]
    # stack []
    # visited 1 2 3 4
    stack = [node]
    while stack:
      curr_node = stack.pop(0)  # I put here -1 instead of 0 first
      # print("curr_node", curr_node.val)
      visited.add(curr_node.val)
      inner_list = []
      for n in curr_node.neighbors:
        if n.val not in visited and n not in stack:
          stack.append(n)
        inner_list.append(n.val)
      res.append(inner_list)
      # print("stack")
      # for s in stack:
      #     print("     ", s.val)
      # print("res", res)
      # yes
      stack.sort(
        key=lambda x: x.val
      )  # Could instead: map -> list where len = len map -> loop over map and put ress in order
      # print("stack")
      # for s in stack:
      #    print("     ", s.val)
    # print(res)

    # [[2],[1,3],[2]]
    # {1: 1[], 2: 2[]}
    # 1[2N]; 2[1N, 3N]; 3[2N]
    mapping = {}
    mapping[1] = Node(1)
    for i, r in enumerate(res, 1):
      curr_node = mapping[i]
      # Old. The else block will execute only once
      # if i in mapping.keys():
      #     curr_node = mapping[i]
      # else: # will execute only once?
      #     curr_node = Node(i)
      #     mapping[i] = curr_node

      for sub_node_val in r:
        if sub_node_val in mapping.keys():
          curr_node.neighbors.append(mapping[sub_node_val])
        else:
          new_node = Node(
            sub_node_val
          )  # could add curr_node, will add in the next loop iteration
          mapping[sub_node_val] = new_node
          curr_node.neighbors.append(new_node)

    return mapping[1]

  def cloneGraph2(self, node: Optional["Node"]) -> Optional["Node"]:
    oldToNew = {}

    def dfs(node):
      if node in oldToNew:
        return oldToNew[node]

      copy = Node(node.val)
      oldToNew[node] = copy
      for nei in node.neighbors:
        copy.neighbors.append(dfs(nei))
      return copy

    return dfs(node) if node else None
