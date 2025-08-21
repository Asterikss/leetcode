from collections import defaultdict, deque


class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    start = m - 1, n - 1
    grid_map = defaultdict(int)
    grid_map[start] = 1
    queue = deque()
    queue.append(start)
    visited = set()

    while queue:
      curr_cell = queue.popleft()
      if curr_cell not in visited:
        visited.add(curr_cell)
        grid_map[curr_cell] += (
          grid_map[curr_cell[0] + 1, curr_cell[1]]
          + grid_map[curr_cell[0], curr_cell[1] + 1]
        )
        if curr_cell[0] - 1 >= 0:
          queue.append((curr_cell[0] - 1, curr_cell[1]))
        if curr_cell[1] - 1 >= 0:
          queue.append((curr_cell[0], curr_cell[1] - 1))

    return grid_map[(0, 0)]

  def uniquePaths2(self, m: int, n: int) -> int:
    row = [1] * n

    for _ in range(m - 1):
      upper_row = [1] * n
      for j in range(n - 2, -1, -1):
        upper_row[j] = upper_row[j + 1] + row[j]
      row = upper_row

    return row[0]
