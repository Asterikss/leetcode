from typing import List, Union
from collections import defaultdict


class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if not n:
      return True
    # [[0, 1], [0, 2], [0, 3], [1, 4]]
    # [[0,1],[2,0],[3,0],[1,4]]
    # 0 123
    # 1 04
    # 2 0
    # 3 0
    # 4 1
    map = defaultdict(set)
    for left, right in edges:
      map[left].add(right)
      map[right].add(left)

    visited = set()

    def dfs(node: int, prev: Union[int, None]):
      if node in visited:
        return False

      visited.add(node)

      if any(not dfs(kid, node) for kid in map[node] if kid != prev):
        return False
      # for kid in map[node]:
      #    if kid != prev and not dfs(kid, node):
      #        return False

      return True

    return dfs(0, None) and len(visited) == n
