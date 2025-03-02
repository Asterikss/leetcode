class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    l, r = 0, 1
    max_length = 0
    helper_set = set()
    while r <= len(s):
      length = r - l
      helper_set.add(s[r - 1])
      if len(helper_set) == length:
        max_length = max(max_length, length)
      else:
        l_update = s[l:r].find(s[r - 1]) + 1
        helper_set.difference_update(s[l : l + l_update - 1])
        l += l_update
        # l = s[l:r-1].rfind(s[r-1]) + 1
        # l = s[:r-1].rfind(s[r-1]) + 1
      r += 1

    return max_length

  def lengthOfLongestSubstring2(self, s: str) -> int:
    l, r = 0, 1
    max_length = 0
    while r <= len(s):
      length = r - l
      if len(set(s[l:r])) == length:  # opt
        max_length = max(max_length, length)
      else:
        l += s[l:r].find(s[r - 1]) + 1
        # l = s[l:r-1].rfind(s[r-1])
        # l = s[:r-1].rfind(s[r-1])
      r += 1

    return max_length

  # This is much more straightforward heh
  def lengthOfLongestSubstring3(self, s: str) -> int:
    charSet = set()
    l = 0
    result = 0
    for r in range(len(s)):
      while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
      charSet.add(s[r])
      result = max(result, r - l + 1)
    return result
