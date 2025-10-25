from typing import List


class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end


class Solution:
  def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    # [(0,30),(5,10),(15,20)]
    # [(5,10),(0,4)]
    LEN_INTERVALS = len(intervals)
    if LEN_INTERVALS == 0:
      return True

    intervals.sort(key=lambda interval: interval.start)

    last_end = intervals[0].end
    for i in range(1, LEN_INTERVALS):
      curr_interval = intervals[i]
      if curr_interval.start < last_end:
        return False
      last_end = curr_interval.end

    return True
