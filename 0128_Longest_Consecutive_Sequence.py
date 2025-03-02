from collections import defaultdict
from typing import List


class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    # 100, 4, 200, 1, 3, 2
    # 100 - 1 | 1
    # 4 - -
    # 3 - -
    # 2 - -
    # 1 - 1+1+1+1 = 4 | 4
    max_length = 0
    nums_set = set(nums)

    for num in nums_set:
      if num - 1 not in nums_set:
        counter = 1
        while num + counter in nums_set:
          counter += 1

          if max_length < counter:
            max_length = counter

    return max_length

  # Takes quite a bit of time for very long sequences
  def longestConsecutive2(self, nums: List[int]) -> int:
    # 2, 20, 4, 10, 3, 4, 5
    # 2 - 4
    # 20 - 1
    # 4 - 4
    # 3 - 4
    # 5 - 4
    m = defaultdict(int)
    for num in nums:
      if m[num] == 0:
        value = 1

        value += m[num - 1]
        value += m[num + 1]

        m[num] = value

        i = 1
        while m[num - i] != 0:
          m[num - i] = value
          i += 1
        i = 1
        while m[num + i] != 0:
          m[num + i] = value
          i += 1
        # or
        # i = 1
        # left = True
        # right = True
        # while m[num + i] != 0 or m[num - i] != 0:
        #     if m[num + i] != 0 and right:
        #         m[num + i] = value
        #     else:
        #         right = False
        #     if m[num - i] != 0 and left:
        #         m[num - i] = value
        #     else:
        #         left = False
        #     i += 1

    return max(m.values()) if m.values() else 0
