from collections import Counter


class Solution:
    # The 4th, but with a dict instead of Counter. Still a bit slower than 3rd
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, k + 1
        max_length = k
        current_length = k + 1

        counter = {}
        for char in s[l:r]:
            counter[char] = counter.get(char, 0) + 1

        while r <= len(s):
            max_freq = max(counter.values(), default=0)
            if current_length - max_freq <= k:
                max_length = max(current_length, max_length)
                current_length += 1
                if r < len(s):
                    counter[s[r]] = counter.get(s[r], 0) + 1
                r += 1
            else:
                counter[s[l]] -= 1
                current_length -= 1
                l += 1

        return max_length


    # 3rd even more optimized
    def characterReplacement2(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res


    # This one just faster (~100ms at least). A lot of it due to not using Counter
    def characterReplacement3(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res


    # With the substring removed as it's unnecessary
    def characterReplacement4(self, s: str, k: int) -> int:
        l, r = 0, k + 1
        max_length = k
        current_length = k + 1

        counter = Counter(s[l:r])
        while r <= len(s):
            if current_length - counter.most_common(1)[0][1] <= k:
                max_length = max(current_length, max_length)
                current_length += 1
                if r < len(s):
                    counter[s[r]] += 1
                r += 1
            else:
                # could skip (l) to the first character that is not the
                # most common character and adjust the r if r-l < k
                counter[s[l]] -= 1
                current_length -= 1
                l += 1

        return max_length


    # With counter not reinitialized everytime
    def characterReplacement5(self, s: str, k: int) -> int:
        l, r = 0, k + 1
        max_length = k

        counter = Counter(s[l:r])
        while r <= len(s):
            substring = s[l:r]
            n_rest = len(substring) - counter.most_common(1)[0][1]
            if n_rest <= k:
                max_length = max(len(substring), max_length)
                if r < len(s):
                    counter[s[r]] += 1
                r += 1
            else:
                counter[substring[0]] -= 1
                l += 1

        return max_length


    # Works, but quite slow
    def characterReplacement6(self, s: str, k: int) -> int:
        l, r = 0, k + 1
        max_length = k

        while r <= len(s):
            substring = s[l:r]
            counter = Counter(substring)
            n_rest = len(substring) - counter.most_common(1)[0][1]
            if n_rest <= k:
                max_length = max(len(substring), max_length)
                r += 1
            else:
                l += 1

        return max_length
