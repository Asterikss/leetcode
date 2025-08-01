from typing import List


class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    LEN_S = len(s)
    word_map = set(wordDict)
    cache = {}

    def dfs(index: int):
      if index in cache:
        return cache[index]
      if index == LEN_S:
        return True

      for end in range(index + 1, LEN_S + 1):
        if s[index:end] in word_map and dfs(end):
          cache[index] = True
          return True

      cache[index] = False
      return False

    return dfs(0)
