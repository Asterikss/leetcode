from typing import List


class Solution:
  def canJump(self, nums: List[int]) -> bool:
    LEN_NUMS = len(nums)
    goal_idx = LEN_NUMS - 1

    # [1,2,0,1,0] 1 + 3 | 3
    for i in range(LEN_NUMS - 2, -1, -1):
      if i + nums[i] >= goal_idx:
        goal_idx = i

    return goal_idx == 0

  def canJump2(self, nums: List[int]) -> bool:
    LEN_NUMS = len(nums)
    helper_arr = [False for _ in range(LEN_NUMS)]
    helper_arr[LEN_NUMS - 1] = True

    for i in range(LEN_NUMS - 2, -1, -1):
      for j in range(1, nums[i] + 1):
        if helper_arr[i + j]:
          helper_arr[i] = True
          break

    return helper_arr[0]

  def canJump3(self, nums: List[int]) -> bool:
    # [1,2,1,0,1]
    # [4,2,1,0,1]
    # [2, 2, 2, 2, 1, 1, 0, 1] false
    LEN_NUMS = len(nums)
    cache = set()

    # [1,2,0,1,0]
    def dfs(index: int):
      if index == LEN_NUMS - 1:
        return True
      if index in cache:
        return False

      for i in range(1, nums[index] + 1):
        if dfs(index + i):
          return True
      cache.add(index)
      return False

    return dfs(0)
