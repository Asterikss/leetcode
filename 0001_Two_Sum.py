from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, v in enumerate(nums):
            if (second := target - v) in map:
                return [i, map[second]]
            map[v] = i

        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            if (second := (target - num)) in nums[i + 1 :]:
                return [i, nums.index(second, i + 1)]

        return []
