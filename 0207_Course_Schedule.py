from collections import defaultdict
from typing import List


class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    reqs = defaultdict(list)
    visited = set()
    for p in prerequisites:
      reqs[p[0]].append(p[1])

    def dfs(start: int):
      if not reqs[start]:
        return True
      if start in visited:
        return False

      visited.add(start)

      for req in reqs[start]:
        if not dfs(req):
          return False
        # reqs[start].remove(req) # Not needed, I can remove all of them at once below
      # visited.remove(start) # I do not need that either, if I check for empty reqs before checking if it was visited before
      reqs[start] = []
      return True

    return all(dfs(start) for start in range(numCourses))

  # Works, but slow
  def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    reqs = defaultdict(list)
    finished = set(i for i in range(numCourses))
    for p in prerequisites:
      reqs[p[0]].append(p[1])
      if p[0] in finished:
        finished.remove(p[0])

    progress = True
    while progress and reqs:
      progress = False
      to_delete = set()
      for k, v in reqs.items():
        for req in v:
          if all(req in finished for req in v):
            finished.add(k)
            to_delete.add(k)
            progress = True

      for to_d in to_delete:
        del reqs[to_d]

    return len(finished) == numCourses
