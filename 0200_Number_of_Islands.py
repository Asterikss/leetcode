from typing import List
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        done = set()
        n_rows_0_based = len(grid) - 1
        row_length_zero_based = len(grid[0]) - 1

        for i, row in enumerate(grid):
            for j, chunk in enumerate(row):
                if chunk == "1" and (i, j) not in done:
                    n_islands += 1
                    stack = [(i, j)]
                    while stack:
                        # print(stack)
                        curr_i, curr_j = stack.pop(0)
                        done.add((curr_i, curr_j))
                        # left
                        if curr_j > 0 and (curr_i, curr_j - 1) not in done and (curr_i, curr_j - 1) not in stack and grid[curr_i][curr_j - 1] == "1":
                            stack.append((curr_i, curr_j - 1))
                        # right
                        if curr_j < row_length_zero_based and (curr_i, curr_j + 1) not in done and (curr_i, curr_j + 1) not in stack and grid[curr_i][curr_j + 1] == "1":
                            stack.append((curr_i, curr_j + 1))
                        # up
                        if curr_i > 0 and (curr_i - 1, curr_j) not in done and (curr_i - 1, curr_j) not in stack and grid[curr_i - 1][curr_j] == "1":
                            stack.append((curr_i - 1, curr_j))
                        # down
                        if curr_i < n_rows_0_based and (curr_i + 1, curr_j) not in done and (curr_i + 1, curr_j) not in stack and grid[curr_i + 1][curr_j] == "1":
                            stack.append((curr_i + 1, curr_j))

        return n_islands

    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n_islands = 0
        done = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(base_row, base_col):
            q = [(base_row, base_col)]
            # q = collections.deque()
            done.add((base_row, base_col))
            while q:
                row, col = q.pop(0) # popleft()
                for d1, d2 in directions:
                    curr_row, curr_col = row + d1, col + d2
                    if (curr_row in range(rows) and
                        curr_col in range(cols) and
                        grid[curr_row][curr_col] == "1" and
                            (curr_row, curr_col) not in done):
                        done.add((curr_row, curr_col))
                        q.append((curr_row, curr_col))

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in done and grid[i][j] == "1":
                    bfs(i, j)
                    n_islands += 1

        return n_islands
