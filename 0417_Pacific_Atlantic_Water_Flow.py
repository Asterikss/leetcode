from typing import Union, List


class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    ROWS = len(heights) - 1
    COLS = len(heights[0]) - 1

    from_pacific = set()
    from_atlantic = set()

    def dfs(i: int, j: int, prev_height: Union[int, float], pacific: bool):
      if i > ROWS or j > COLS or i < 0 or j < 0 or heights[i][j] < prev_height:
        return

      if pacific:
        if (i, j) in from_pacific:
          return
        from_pacific.add((i, j))
      else:
        if (i, j) in from_atlantic:
          return
        from_atlantic.add((i, j))

      dfs(i - 1, j, heights[i][j], pacific)
      dfs(i + 1, j, heights[i][j], pacific)
      dfs(i, j - 1, heights[i][j], pacific)
      dfs(i, j + 1, heights[i][j], pacific)

    for i in range(ROWS + 1):
      dfs(i, 0, float("-inf"), True)  # Pacific
      dfs(i, COLS, float("-inf"), False)  # Atlantic
    for i in range(COLS):
      dfs(0, i + 1, float("-inf"), True)  # Pacific
      dfs(ROWS, i, float("-inf"), False)  # Atlantic

    return list(from_pacific & from_atlantic)

  # very slighltly optimized solution
  def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
    ret = set()
    ROWS = len(heights) - 1
    COLS = len(heights[0]) - 1

    def dfs(i: int, j: int, prev_height: Union[int, float]) -> bool:
      nonlocal pacific, atlantic
      if (
        i > ROWS
        or j > COLS
        or i < 0
        or j < 0
        or (i, j) in visited
        or heights[i][j] > prev_height
      ):
        return False

      if (i, j) in ret:
        return True

      if not pacific and (i == 0 or j == 0):
        pacific = True
      if not atlantic and (i == ROWS or j == COLS):
        atlantic = True

      if pacific and atlantic:
        return True

      visited.add((i, j))

      return (
        dfs(i - 1, j, heights[i][j])
        or dfs(i + 1, j, heights[i][j])
        or dfs(i, j - 1, heights[i][j])
        or dfs(i, j + 1, heights[i][j])
      )

    for i, row in enumerate(heights):
      for j in range(len(row)):
        visited = set()
        pacific = False
        atlantic = False
        if dfs(i, j, float("inf")):
          ret.add((i, j))

    return list(ret)
