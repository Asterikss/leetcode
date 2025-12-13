import math
from typing import List


class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    # new_row, new_col = old_col, len(row) - 1 - old_row
    N = len(matrix) - 1

    def change_place(orig_row, orig_col, value_to_place, n_times):
      new_row, new_col = orig_col, N - orig_row
      n_times -= 1
      substituted_value = matrix[new_row][new_col]
      matrix[new_row][new_col] = value_to_place
      if n_times > 0:
        change_place(new_row, new_col, substituted_value, n_times)

    for j in range(math.ceil(N / 2)):
      for i in range(j, N - j):
        change_place(j, i, matrix[j][i], 4)
