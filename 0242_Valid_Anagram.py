from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ts, ss = {}, {}
        for i in range(len(t)):
            ts[t[i]] = 1 + ts.get(t[i], 0)
            ss[s[i]] = 1 + ss.get(s[i], 0)

        for val in ts:
            if ts[val] != ss.get(val, 0):
                return False
        return True


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
