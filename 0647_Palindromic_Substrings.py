class Solution:
  def countSubstrings(self, s: str) -> int:
    LEN_S = len(s)
    n_palindromes = 0

    for i in range(LEN_S):
      # odd
      l, r = i, i
      while l >= 0 and r < LEN_S and s[l] == s[r]:
        n_palindromes += 1
        l -= 1
        r += 1

      # even
      l, r = i, i + 1
      while l >= 0 and r < LEN_S and s[l] == s[r]:
        n_palindromes += 1
        l -= 1
        r += 1

    return n_palindromes
