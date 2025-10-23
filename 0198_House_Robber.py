from typing import List


class Solution:
  def rob(self, nums: List[int]) -> int:
    # [1,1,3,3]
    # 0,0[2,9,8,3,6]
    prev_prev_house, prev_house = 0, 0

    #   [8,         3,          6]]
    # [prev_prev_house, prev_house, n, n+1]
    #                   [pph,       ph, n, n+1]
    #   [1,1,3,3]
    #        4,4
    for n in nums:
      tmp_prev = prev_house
      prev_house = max(prev_prev_house + n, prev_house)
      prev_prev_house = tmp_prev

    return prev_house

  # too slow
  def rob4(self, nums: List[int]) -> int:
    max_amount = 0
    # [1, 3, 1, 4, 9]
    # 1 11
    # 3
    # [9, 1, 0, 9, 80]
    # [9, 1, 0, 9]
    # [9, 1, 0, 80, 9]
    # [9, 7, 0, 6, 80, 900, 1]

    def rob(idx: int, amount: int):
      nonlocal max_amount
      if idx >= len(nums):
        return
      amount += nums[idx]
      max_amount = max(max_amount, amount)

      rob(idx + 2, amount)
      rob(idx + 3, amount)

    rob(0, 0)
    rob(1, 0)

    return max_amount
