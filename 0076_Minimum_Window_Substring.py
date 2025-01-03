from collections import Counter


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if t == "":
      return ""
    return_l, return_r = None, None

    l, r = 0, 0
    dict_t = {}
    for ch in t:
      dict_t[ch] = dict_t.get(ch, 0) + 1
    t_needed = len(dict_t)
    t_have = 0

    dict_curr = {}
    # "ADOBECODEBANC"
    # "ABC"
    #  DOBECODEBA
    while r < len(s) + 1:
      if t_needed == t_have:
        if return_l is None:  # and return_r is None
          return_l = l
          return_r = r
        elif (return_r - return_l) > (r - l):
          return_l = l
          return_r = r
        if s[l] in dict_t:
          dict_curr[s[l]] -= 1
          if dict_curr[s[l]] < dict_t[s[l]]:
            t_have -= 1
        l += 1
        # print("in l")
      else:
        if r < len(s):
          curr_char = s[r]
          if curr_char in dict_t:
            dict_curr[curr_char] = dict_curr.get(curr_char, 0) + 1
            if dict_curr[curr_char] == dict_t[curr_char]:
              t_have += 1
        r += 1
        # print("in r")
      # print(dict_curr, t_needed, t_have, dict_t, l, r)

    # print(return_l, return_r)
    if not return_l and not return_r:
      return ""
    return s[return_l:return_r]

  # Much cleaner, a litle bit faster, using float("inf") and not None etc. ehh
  def minWindow2(self, s: str, t: str) -> str:
    if t == "":
      return ""

    countT, window = {}, {}

    for c in t:
      countT[c] = countT.get(c, 0) + 1

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("inf")
    l = 0
    for r in range(len(s)):
      c = s[r]
      window[c] = window.get(c, 0) + 1  # why c in countT check not before this?

      if c in countT and window[c] == countT[c]:
        have += 1

      while have == need:
        if (r - l + 1) < resLen:
          res = [l, r]
          resLen = r - l + 1
        window[s[l]] -= 1
        if s[l] in countT and window[s[l]] < countT[s[l]]:
          have -= 1
        l += 1

    l, r = res
    return s[l : r + 1] if resLen != float("inf") else ""

  def minWindow3(self, s: str, t: str) -> str:
    l, r = 0, len(t)
    ret = None
    dict_t = Counter(t)

    dict_subs = Counter(s[l:r])
    while r < len(s) + 1 and l < r:
      curr_subs = s[l:r]
      if len(dict_t - dict_subs) == 0:
        if ret is None:
          ret = curr_subs
        elif len(ret) > len(curr_subs):
          ret = curr_subs
        dict_subs[s[l]] -= 1
        l += 1
      else:
        if r < len(s):
          dict_subs[s[r]] += 1
        r += 1

    return ret if ret else ""

  def minWindow4(self, s: str, t: str) -> str:
    l, r = 0, len(t)
    ret = None
    dict_t = Counter(t)

    # "OUZODYXAZV"
    # "XYZ"
    # XAZV
    while r < len(s) + 1 and l < r:
      curr_subs = s[l:r]
      if len(dict_t - Counter(curr_subs)) == 0:
        if ret is None:
          ret = curr_subs
        elif len(ret) > len(curr_subs):
          ret = curr_subs
        l += 1
      else:
        r += 1

    return ret if ret else ""
