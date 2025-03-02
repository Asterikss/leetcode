from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    l, r = 0, 1
    while r < len(prices):
      current_profit = prices[r] - prices[l]
      if current_profit < 0:
        l, r = l + 1, r + 1
        continue
      if current_profit > max_profit:
        max_profit = current_profit
      r += 1

    return max_profit


class Solution2:
  def maxProfit(self, prices: List[int]) -> int:
    sorted_prices = sorted(prices)
    max_val = 0
    print(sorted_prices)
    print(prices)
    print("----")
    for sp in sorted_prices:
      print("--")
      biggest_idx = -1
      smallest_idx = prices.index(sp)
      print(sp, smallest_idx, biggest_idx)
      while smallest_idx > self.list_rindex(prices, sorted_prices[biggest_idx]):
        biggest_idx -= 1
      print(sp, smallest_idx, biggest_idx)
      if (new_max := sorted_prices[biggest_idx] - sp) > max_val:
        max_val = new_max
      print(new_max)
      print("--")

    return max_val

  def list_rindex(self, li, x):
    for i in reversed(range(len(li))):
      if li[i] == x:
        return i
    raise ValueError("{} is not in list".format(x))
