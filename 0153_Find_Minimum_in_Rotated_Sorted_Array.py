from typing import List


class Solution:
  def findMin(self, nums: List[int]) -> int:
    # [3,4,5,6,1,2]
    # [3,4,5,6,7,1,2]
    # [2,3,4,5,6,1]
    # [4,5,0,1,2,3]
    # [4,5,6,7]

    if nums[0] <= nums[-1]:
      return nums[0]

    curr_idx = len(nums) - 1
    new_idx = curr_idx // 2
    while True:
      if nums[curr_idx - 1] > nums[curr_idx]:
        return nums[curr_idx]

      if nums[new_idx] < nums[curr_idx]:
        curr_idx = new_idx
      else:
        curr_idx -= 1

      new_idx = (curr_idx + new_idx) // 2

  def findMin2(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
      mid = (l + r) // 2

      if nums[mid] >= nums[r]:
        l = mid + 1
      else:
        r = mid
    return nums[l]

  def findMin3(self, nums: List[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1
    while l <= r:
      if nums[l] < nums[r]:
        res = min(res, nums[l])
        break
      m = (l + r) // 2
      res = min(res, nums[m])
      if nums[m] >= nums[l]:  # part of left portion
        l = m + 1
      else:
        r = m - 1

    return res
