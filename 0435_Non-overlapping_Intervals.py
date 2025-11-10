from typing import List


class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda interval: interval[1])
    min_to_remove = 0
    # [[1,2],[2,4],[1,4]]
    # [[1,3],[2,4],[1,4]]

    prev_end = intervals[0][1]
    for i in range(1, len(intervals)):
      if intervals[i][0] < prev_end:
        min_to_remove += 1
      else:
        prev_end = intervals[i][1]

    return min_to_remove
