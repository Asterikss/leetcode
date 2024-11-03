from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            helper_table = [0 for _ in range(26)]
            for letter in s:
                helper_table[ord(letter) - 97] += 1
            m[tuple(helper_table)].append(s)

        return list(m.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            m[''.join(sorted(s))].append(s)

        return list(m.values())
