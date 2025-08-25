from typing import List
import bisect


class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    LEN_NUMS = len(nums)
    max_len = 1
    cache = [1] * LEN_NUMS

    for index in range(LEN_NUMS - 2, -1, -1):
      curr_val = nums[index]
      for i in range(index + 1, LEN_NUMS):
        if nums[i] > curr_val:
          prev_length = cache[i]
          should_break = prev_length == max_len
          new_length = prev_length + 1
          cache[index] = max(cache[index], new_length)
          max_len = max(max_len, new_length)
          if should_break:
            break

    return max_len

  def lengthOfLIS2(self, nums: List[int]) -> int:
    LEN_NUMS = len(nums)
    cache = [1] * LEN_NUMS

    for i in range(LEN_NUMS - 1, -1, -1):
      for j in range(i + 1, LEN_NUMS):
        if nums[j] > nums[i]:
          cache[i] = max(cache[i], 1 + cache[j])

    return max(cache)

  def lengthOfLISAAAAAAAclose(self, nums: List[int]) -> int:
    # need to search for the max length that is bigger than curr_val
    # sort -> index + 1
    LEN_NUMS = len(nums)
    max_len = 1
    last_number = nums[LEN_NUMS - 1]
    cache = {last_number: 1}
    sorted_parsed_numbers = [last_number]
    len_sorted_parsed_numbers = 1
    parsed_numbers = set([last_number])

    for index in range(LEN_NUMS - 2, -1, -1):
      curr_val = nums[index]

      # sorted_index = bisect.bisect_left(sorted_parsed_numbers, curr_val)
      sorted_index = bisect.bisect_right(sorted_parsed_numbers, curr_val)
      # if curr_val == 3:
      #     print(sorted_index)
      #     print(cache)
      #     print(sorted_parsed_numbers)
      #     print(len_sorted_parsed_numbers)
      # if sorted_index + 1 < len_sorted_parsed_numbers:
      if sorted_index < len_sorted_parsed_numbers:
        # new_length = cache.get(sorted_parsed_numbers[sorted_index + 1], 1) + 1
        new_length = cache.get(sorted_parsed_numbers[sorted_index], 1) + 1
        # if curr_val == 3:
        #     print("update with:", new_length)
        max_len = max(max_len, new_length)
        cache[curr_val] = new_length

      if curr_val not in parsed_numbers:
        sorted_parsed_numbers.insert(sorted_index, curr_val)
        parsed_numbers.add(curr_val)
        len_sorted_parsed_numbers += 1

      # if curr_val == 3:
      #     print(sorted_parsed_numbers)

    # print(cache)
    return max_len
