from typing import List


class Solution:
  def coinChange(self, coins: List[int], amount: int):
    # for this amount -> how many coins needed
    cache = {i: float("inf") for i in range(amount + 1)}
    cache[0] = 0

    # i - coin
    # 7  3 -> 4 (7-3)
    # [1,2,5],
    # [7,2,5],
    for i in range(1, amount + 1):
      for coin in coins:
        if i - coin >= 0:
          cache[i] = min(cache[i - coin] + 1, cache[i])

    return cache[amount] if cache[amount] != float("inf") else -1

  def coinChange2(self, coins: List[int], amount: int):
    # cache[to compute this amout] = it takes this many coins
    cache = [float("inf")] * (amount + 1)  # 0..amount
    cache[0] = 0

    # [1,2,5], 11
    for a in range(1, amount + 1):
      for coin in coins:
        if a - coin >= 0:
          cache[a] = min(cache[a - coin] + 1, cache[a])

    return cache[amount] if cache[amount] != float("inf") else -1

  def coinChange3(self, coins: List[int], amount: int):
    cache = {i: float("inf") for i in range(amount + 1)}
    cache[0] = 0
    for i in range(1, amount + 1):
      for coin in coins:
        cache[i] = min(cache.get(i - coin, float("inf")) + 1, cache[i])
    return cache[amount] if cache[amount] != float("inf") else -1
