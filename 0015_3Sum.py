from typing import List


class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3:
      return []

    results = []

    nums_sorted = sorted(nums)
    nums_length = len(nums)
    a = 0
    # [-1,0,1,2,-1,-4]
    # -4 -1 -1 0 1 2
    while a < nums_length - 2:
      if nums_sorted[a] > 0:
        break

      if a != 0 and nums_sorted[a - 1] == nums_sorted[a]:
        a += 1
        continue

      l = a + 1
      r = nums_length - 1

      while l < r:
        # print("A", a, l , r, results)
        if (
          tmp_sum := sum(tmp := [nums_sorted[a], nums_sorted[l], nums_sorted[r]])
        ) == 0:
          results.append(tmp)
          l += 1
          while l < r and nums_sorted[l] == nums_sorted[l - 1]:
            l += 1
        elif tmp_sum > 0:
          r -= 1
          # not needed here
          # while l < r and nums_sorted[r] == nums_sorted[r + 1]:
          #   r -= 1
        else:
          l += 1
          # not needed here
          # while l < r and nums_sorted[l] == nums_sorted[l - 1]:
          #     l += 1
        # print("B", a, l, r, results)
      a += 1

    return results

  # works but too slow
  def threeSum2(self, nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3:
      return []

    results = []

    nums_sorted = sorted(nums)
    a = 0
    nums_length = len(nums)
    while a < nums_length - 2:
      if nums_sorted[a] > 0:
        break
      if a != 0 and nums_sorted[a - 1] == nums_sorted[a]:
        a += 1
        continue

      b = a + 1
      while b < nums_length - 1:
        if b > a + 1 and nums_sorted[b - 1] == nums_sorted[b]:
          b += 1
          continue
        c = b + 1
        while c < nums_length:
          if c > b + 1 and nums_sorted[c - 1] == nums_sorted[c]:
            c += 1
            continue
          if sum(tmp := [nums_sorted[a], nums_sorted[b], nums_sorted[c]]) == 0:
            # if tmp not in results:
            #    results.append(tmp)
            results.append(tmp)
          c += 1
        b += 1
      a += 1

    return results

  # works but too slow
  def threeSum3(self, nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3:
      return []

    results = []

    a = 0
    while a < len(nums) - 2:
      b = a + 1
      while b < len(nums) - 1:
        c = b + 1
        while c < len(nums):
          if nums[a] + nums[b] + nums[c] == 0:
            tmp = sorted([nums[a], nums[b], nums[c]])
            if tmp not in results:
              results.append(tmp)
          c += 1
        b += 1
      a += 1

    return results
