from typing import List


class Solution:
  # this one is a little bit cursed
  def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    flipped = False
    if nums[0] == target:
      return 0
    if nums[0] > target:
      flipped = True

    while l != r:
      mid = (r - l) // 2 + l
      curr_val = nums[mid]
      # print(mid, curr_val, l, r)
      if curr_val == target:
        return mid
      if r - 1 == l:
        break
      if curr_val > target:
        if flipped:  # not flipped and ...
          if curr_val > nums[r - 1]:
            l = mid  # go right
          else:
            r = mid  # go left still
        else:
          r = mid  # go left as usual
      else:
        if not flipped:  # flipped and ...
          if curr_val > nums[l]:
            l = mid  # go right
          else:
            r = mid  # go left
        else:
          l = mid  # go right like usual

    return -1

  # same, but with comments left
  def search2(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    flipped = False
    if nums[0] == target:
      return 0
    if nums[0] > target:
      flipped = True

    # [3,4,5,6,1,2] | 1
    #          |
    # l 4 r 6 mid 4
    # [3,5,6,0,1,2], target = 4
    # l 5 r 6 mid
    while l != r:
      mid = (r - l) // 2 + l
      curr_val = nums[mid]
      # print(mid, curr_val, l, r)
      if curr_val == target:
        return mid
      if r - 1 == l:
        # print("break")
        # [4,5,6,7,8,9,2] 2
        # [3,5,6,0,1,2,3] 1
        # [3,5,6,0,1,2, ]
        break
      if curr_val > target:
        if flipped:
          if curr_val > nums[r - 1]:
            l = mid  # go right
          else:
            r = mid  # go left
        else:
          r = mid  # go left
      else:
        # [3,5,6,0,1,2] 6 # not flipped - left
        # [3,5,-1,0,1,2] 6 # not flipped - left
        # [3,5,6,0,1,2] 2 # filled - rightk
        # [3,4,5,6,7,8] 4
        # [6,7,8,9,0,1,2,3,4] 9
        if not flipped:
          if curr_val > nums[l]:
            l = mid  # go right
          else:
            r = mid  # go left
        else:
          l = mid  # go right like usual

    return -1
