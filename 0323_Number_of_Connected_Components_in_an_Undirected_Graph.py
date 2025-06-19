from collections import defaultdict
from typing import List


class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    hmap = defaultdict(list)
    for left, right in edges:
      hmap[left].append(right)
      hmap[right].append(left)

    visited = set()
    components: int = 0

    def dfs(node: int):
      if node in visited:
        return
      visited.add(node)
      for kid in hmap[node]:
        dfs(kid)

    for i in range(n):
      if i not in visited:
        components += 1
        dfs(i)

    return components

  # [[0,1], [0,2]]
  # 0 1 2
  # 1 0
  # 2 0
  # [[0,1], [1,2], [2,3], [4,5]]
  # 0 1
  # 1 0 2
  # 2 1 3
  # 3 2
  # 4 5
  # 5 4
  # [[0,1], [1,2], [2,3], [-1,0], [0, -2], [4,5]]
  # -2 0
  # -1 0
  # 0 1 -1 -2
  # 1 0 2
  # 2 3 1
  # 3 2
  # 4 5

  # Union find
  def countComponents2(self, n: int, edges: List[List[int]]) -> int:
    parent = [i for i in range(n)]
    rank = [1] * n

    def find(n1):
      res = n1

      while res != parent[res]:
        parent[res] = parent[parent[res]]
        res = parent[res]
      return res

    def union(n1, n2):
      parent1, parent2 = find(n1), find(n2)
      if parent1 == parent2:
        return 0

      if rank[parent2] > rank[parent1]:
        parent[parent1] = parent2
        rank[parent2] += rank[parent1]
      else:
        parent[parent2] = parent1
        rank[parent1] += rank[parent2]
      return 1

    res = n
    for n1, n2 in edges:
      res -= union(n1, n2)
    return res
