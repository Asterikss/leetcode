from typing import List


class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    ret = []

    intervals.sort(key=lambda interval: interval[0])

    prev_start = intervals[0][0]
    prev_end = intervals[0][1]
    # [[1,3],[1,5],[6,7]]
    for i in range(1, len(intervals)):
      if intervals[i][0] > prev_end:
        ret.append([prev_start, prev_end])
        prev_start = intervals[i][0]
        prev_end = intervals[i][1]
      else:
        prev_end = max(prev_end, intervals[i][1])

    ret.append([prev_start, prev_end])

    return ret
