from typing import List


class Solution:
  def maxArea(self, height: List[int]) -> int:
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
      height_l_pointer = height[l]
      height_r_pointer = height[r]
      min_height = min(height_l_pointer, height_r_pointer)

      area = (r - l) * min_height
      if area > max_area:
        max_area = area

      if height_l_pointer <= height_r_pointer:
        l += 1
      else:
        r -= 1

    return max_area
