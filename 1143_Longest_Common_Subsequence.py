from collections import defaultdict


class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    grid = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
    for i in range(len(text1) - 1, -1, -1):
      for j in range(len(text2) - 1, -1, -1):
        if text1[i] == text2[j]:
          grid[j][i] = 1 + grid[j + 1][i + 1]
        else:
          grid[j][i] = max(grid[j + 1][i], grid[j][i + 1])

    return grid[0][0]

  # passed 20/22
  def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
    max_len = 0
    letter_idxs = defaultdict(list)
    for i, l in enumerate(text2):
      letter_idxs[l].append(i)

    # "cat"
    # "crabt"
    # c 0 r 1 a 2 b 3 t 4
    for i in range(len(text1)):
      curr_subsequence_len = 0
      prev_index = -1

      for letter in text1[i:]:
        if letter not in letter_idxs:
          continue

        min_bigger_idx = float("inf")
        for idx in letter_idxs[letter]:
          if idx > prev_index and idx < min_bigger_idx:
            min_bigger_idx = idx

        if min_bigger_idx == float("inf"):
          continue

        prev_index = min_bigger_idx
        curr_subsequence_len += 1
        max_len = max(max_len, curr_subsequence_len)

    return max_len
