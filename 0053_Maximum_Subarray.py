from typing import List


class Solution:
  def maxSubArray(self, nums: List[int]) -> int | float:
    max_sum = float("-inf")
    LEN_NUMS = len(nums)
    # 7 5 8 4 6 4 3 4
    # 2 -1| 4 2 4 5 4 8

    sum_val = 0
    for i in range(LEN_NUMS - 1, -1, -1):
      curr_val = nums[i]
      sum_val += curr_val
      if curr_val > 0:
        max_sum = max(max_sum, sum_val)
      elif sum_val < 0:
        sum_val = 0

    return max_sum if max_sum != float("-inf") else max(nums)

  def maxSubArray2(self, nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
      if cur_sum < 0:
        cur_sum = 0
      cur_sum += n
      max_sum = max(max_sum, cur_sum)

    return max_sum
