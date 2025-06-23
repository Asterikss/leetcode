class Solution:
  def longestPalindrome(self, s: str) -> str:
    LEN_S = len(s)
    max_palindrome = ""
    len_max_palindrome = 0

    for i in range(LEN_S):
      # odd
      l, r = i, i
      while l >= 0 and r < LEN_S and s[l] == s[r]:
        if (r - l + 1) > len_max_palindrome:
          max_palindrome = s[l : r + 1]
          len_max_palindrome = r - l + 1
        l -= 1
        r += 1
      # even
      l, r = i, i + 1
      while l >= 0 and r < LEN_S and s[l] == s[r]:
        if (r - l + 1) > len_max_palindrome:
          max_palindrome = s[l : r + 1]
          len_max_palindrome = r - l + 1
        l -= 1
        r += 1

    return max_palindrome

  # works, but on the slower side
  def longestPalindrome2(self, s: str) -> str:
    LEN_S = len(s)
    max_palindrome = ""
    len_max_palindrome = 0

    # "ababd"
    # a -> ab
    # b -> {aba} abab
    # a -> ab [bab] babd ababd
    # b -> bd abd
    # d -> -
    def is_palindrome(string: str) -> bool:
      return string == string[::-1]

    for i in range(LEN_S):
      l, r = i, i + 1
      while True:
        r += 1
        if r > LEN_S:
          break

        if (
          len_max_palindrome < r - l
          and s[l] == s[r - 1]
          and is_palindrome((slice := s[l:r]))
        ):
          max_palindrome = slice
          len_max_palindrome = len(slice)

        l -= 1
        if l < 0:
          break

        if (
          len_max_palindrome < r - l
          and s[l] == s[r - 1]
          and is_palindrome((slice := s[l:r]))
        ):
          max_palindrome = slice
          len_max_palindrome = len(slice)

    return max_palindrome if max_palindrome else s[0]

  # works, but on the slower side
  def longestPalindrome3(self, s: str) -> str:
    LEN_S = len(s)
    max_palindrome = ""
    len_max_palindrome = 0

    def is_palindrome(string: str) -> bool:
      return string == string[::-1]

    def find_palindrome(start: int, stop: int):
      nonlocal len_max_palindrome, max_palindrome
      if start >= stop:
        return

      substring = s[start:stop]
      if len(substring) <= len_max_palindrome:
        return

      if is_palindrome(substring):
        max_palindrome = substring
        len_max_palindrome = len(substring)
      else:
        find_palindrome(start, stop - 1)

    for i in range(LEN_S):
      find_palindrome(i, LEN_S)

    return max_palindrome
