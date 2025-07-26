from typing import List


class Solution:
  def maxProduct(self, nums: List[int]):
    # [1,2,-3,4]
    max_product = float("-inf")
    min_val, max_val = 1, 1

    for num in nums:
      tmp_min_val = min_val
      min_val = min(num * min_val, num * max_val, num)
      max_val = max(num * max_val, num * tmp_min_val, num)
      max_product = max(max_product, max_val)

    return max_product

  def maxProduct70(self, nums: List[int]):
    LEN_NUMS = len(nums)
    max_product = float("-inf")
    for i in range(LEN_NUMS):
      product = 1
      is_positive = True
      max_r = -1
      r = i
      while r < LEN_NUMS:
        curr_num = nums[r]
        if curr_num == 0:
          max_product = max(max_product, 0)
          break
        if curr_num < 0:
          is_positive = not is_positive
        if is_positive and r > max_r:
          max_r = r
        r += 1
      if max_r != -1:
        product = 1
        for n in nums[i : max_r + 1]:
          product *= n
        max_product = max(max_product, product)

    # Can only be -inf if nums has just one number and it’s negative, or if all numbers are zeros.
    if max_product == float("-inf"):
      return nums[0]
    return max_product
