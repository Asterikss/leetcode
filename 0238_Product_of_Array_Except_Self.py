from typing import List


class Solution:
  # Could also use just one array instead of two
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    pre = [0 for _ in range(len(nums))]
    suff = [0 for _ in range(len(nums))]

    curr_prod = 1
    for i, num in enumerate(nums):
      pre[i] = curr_prod
      curr_prod *= num

    curr_prod = 1
    for i, num in enumerate(nums[::-1], 1):
      suff[-i] = curr_prod
      curr_prod *= num

    for i in range(len(pre)):
      pre[i] *= suff[i]

    return pre

  # O(n) but using /
  def productExceptSelf2(self, nums: List[int]) -> List[int]:
    ret = [0 for _ in range(len(nums))]
    n_zeros = 0
    product = 1

    for num in nums:
      if num != 0:
        product *= num
      else:
        n_zeros += 1

    for i, num in enumerate(nums):
      if num != 0:
        if not n_zeros:
          ret[i] = product // num
      else:
        if n_zeros == 1:
          ret[i] = product

    return ret
