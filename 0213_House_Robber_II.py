from typing import List


class Solution:
  # I thought rob2 is cheating, so... siu
  def rob(self, nums: List[int]) -> int:
    NUMS_LEN = len(nums)
    memo = dict()

    def dfs(index: int, used_last: bool | None):
      if index < 0:
        return 0
      if index == 0 and used_last:
        return 0
      if (index, used_last) in memo:
        return memo[(index, used_last)]

      if index == NUMS_LEN - 1:
        result1 = dfs(index - 2, True) + nums[index]
      else:
        result1 = dfs(index - 2, used_last) + nums[index]
      result2 = dfs(index - 1, used_last)
      result3 = dfs(index - 2, used_last)  # skip first house

      result = max(result1, result2, result3)
      memo[(index, used_last)] = result

      return result

    return dfs(NUMS_LEN - 1, False)

  def rob2(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    prev_prev_house, prev_house = 0, 0

    for n in nums[1:]:
      tmp_prev_house = prev_house
      prev_house = max(prev_prev_house + n, prev_house)
      prev_prev_house = tmp_prev_house

    first_skipped = prev_house

    prev_prev_house, prev_house = 0, 0
    for n in nums[:-1]:
      tmp_prev_house = prev_house
      prev_house = max(prev_prev_house + n, prev_house)
      prev_prev_house = tmp_prev_house

    return max(first_skipped, prev_house)
