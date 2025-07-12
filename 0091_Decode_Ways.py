class Solution:
  def numDecodings(self, s: str) -> int:
    if not s or s[0] == "0":
      return 0

    prev2 = prev1 = 1  # [i-2], [i-1]

    for i in range(1, len(s)):
      current = 0

      if s[i] != "0":
        current += prev1

      if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] <= "6"):
        current += prev2

      prev2, prev1 = prev1, current

    return prev1

  def numDecodings2(self, s: str) -> int:
    LEN_S = len(s)
    if not s:
      return 0

    n_ways = 0

    def dfs(index: int):
      nonlocal n_ways
      if index == LEN_S:
        n_ways += 1
        return

      if s[index] == "0":
        return

      dfs(index + 1)

      if index + 1 < LEN_S:
        if s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456"):
          dfs(index + 2)

    dfs(0)
    return n_ways
