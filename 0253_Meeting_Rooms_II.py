import bisect
from typing import List


class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end


def print_days_data(days_data):
  for day_idx, intervals in enumerate(days_data, start=1):
    print(f"Day {day_idx}: [", end="")
    print(", ".join(f"({i.start}, {i.end})" for i in intervals), end="")
    print("]")


class Solution:
  # This is something. Works? Works.
  def minMeetingRooms(self, intervals: List[Interval]) -> int:
    LEN_INTERVALS = len(intervals)
    if LEN_INTERVALS < 1:
      return 0
    intervals.sort(key=lambda interv: interv.start)

    inserted = False
    days_data = [[intervals[0]]]
    for i in range(1, LEN_INTERVALS):
      inserted = False
      curr_interval = intervals[i]
      for day_data in days_data:
        #  [(0,40),(5,10)]   ,(15,20)]
        index = bisect.bisect_left(
          day_data, curr_interval.start, key=lambda itv: itv.start
        )
        if index >= 1 and day_data[index - 1].end > curr_interval.start:
          continue
        if index < len(day_data) and day_data[index].start < curr_interval.end:
          continue
        inserted = True
        bisect.insort(day_data, curr_interval, key=lambda itv: itv.start)
        break

      if not inserted:
        days_data.append([curr_interval])

    # print_days_data(days_data)
    return len(days_data)

  def minMeetingRooms2(self, intervals):
    start_vals = sorted([i.start for i in intervals])
    end_vals = sorted([i.end for i in intervals])

    max_count, curr_count = 0, 0
    start_vals_idx, end_vals_idx = 0, 0
    while start_vals_idx < len(start_vals):
      if start_vals[start_vals_idx] < end_vals[end_vals_idx]:
        start_vals_idx += 1
        curr_count += 1
        max_count = max(max_count, curr_count)
      else:
        end_vals_idx += 1
        curr_count -= 1

    return max_count
