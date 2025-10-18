from typing import List


class Solution:
  # The greatest solution on Earth. 2 am coding. O(1) memory btw
  def insert2(
    self, intervals: List[List[int]], newInterval: List[int]
  ) -> List[List[int]]:
    LEN_INTERVALS = len(intervals)
    has_been_inserted = False

    # [[1,3],[4,6]] | [2,5]
    # [[1,2],[4,6]]
    # [[1,2],[3,5],[9,10]], newInterval = [6,7]
    for i, interval in enumerate(intervals):
      if newInterval[0] >= interval[0]:
        # not before the current interval
        if newInterval[0] <= interval[1]:
          # not after the current interval - new interval start inside of the current interval
          if i + 1 >= LEN_INTERVALS or intervals[i + 1][0] > newInterval[1]:
            # extend the current interval to the end of the newIntereval
            intervals[i][1] = max(newInterval[1], intervals[i][1])
          else:
            # merge with the next interval
            popped_interval = intervals.pop(i + 1)
            LEN_INTERVALS -= 1
            # newInterval could span multiple intervals
            j = i
            while j + 1 < LEN_INTERVALS and intervals[j + 1][0] <= newInterval[1]:
              popped_interval = intervals.pop(j + 1)
              LEN_INTERVALS -= 1

            intervals[i][1] = max(popped_interval[1], newInterval[1])

          has_been_inserted = True
          break
        else:
          # after the current interval
          continue
      else:
        # before the current interval
        if newInterval[1] < interval[0]:
          # newInterval does not touch the current interval -> it should be before the current one
          intervals.insert(i, newInterval)
        else:
          if newInterval[1] <= interval[1]:
            # e.g., intervals=[[1,5]] newInterval=[0,3]
            # newInterval touchs the current interval - merged them
            intervals[i][0] = min(intervals[i][0], newInterval[0])
            intervals[i][1] = interval[1]
          else:
            # e.g., intervals=[[1,5]] newInterval=[0,6]
            # newInterval is inside the current interval and surpasses it
            j = i
            popped_interval = None
            while j + 1 < LEN_INTERVALS and intervals[j + 1][0] <= newInterval[1]:
              popped_interval = intervals.pop(j + 1)
              LEN_INTERVALS -= 1

            intervals[i][0] = min(intervals[i][0], newInterval[0])
            if popped_interval:
              intervals[i][1] = max(popped_interval[1], newInterval[1])
            else:
              intervals[i][1] = newInterval[1]

        has_been_inserted = True
        break

    if not has_been_inserted:
      intervals.append(newInterval)

    return intervals

  def insert(
    self, intervals: List[List[int]], newInterval: List[int]
  ) -> List[List[int]]:
    ret = []
    new_start, new_end = newInterval
    LEN_INTERVALS = len(intervals)
    i = 0

    # [[1,3],[4,6]] | [2,5]
    while i < LEN_INTERVALS and intervals[i][1] < new_start:
      ret.append(intervals[i])
      i += 1

    while i < LEN_INTERVALS and intervals[i][0] <= new_end:
      new_start = min(intervals[i][0], new_start)
      new_end = max(intervals[i][1], new_end)
      i += 1
    ret.append([new_start, new_end])

    while i < LEN_INTERVALS:
      ret.append(intervals[i])
      i += 1

    return ret
