from typing import List


class Solution:
  def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    ret = []

    def get_sums(curr_sum, curr_index, sequence):
      if curr_sum > target:
        return
      elif curr_sum == target:
        ret.append(sequence)
        return

      for i, n in enumerate(nums[curr_index:]):
        get_sums(curr_sum + n, i + curr_index, sequence + [n])

    for j, n in enumerate(nums):
      get_sums(n, j, [n])

    return ret
