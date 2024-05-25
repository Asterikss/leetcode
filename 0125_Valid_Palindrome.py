class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.is_alnum(s[l]) and l < r:
                l += 1
            while not self.is_alnum(s[r]) and l < r:
                r -= 1

            # print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False

            l, r = l+1, r-1

        return True


    def is_alnum(self, ch):
        ch_ord = ord(ch)
        return (ord("A") <= ch_ord <= ord("Z")) or (ord("a") <= ch_ord <= ord("z")) or  (ord("0") <= ch_ord <= ord("9"))


class Solution2:
    def isPalindrome(self, s: str) -> bool:
      x = ''.join(c for c in s.lower() if c.isalnum())
      # isalpha() & isdigit())
      return x == x[::-1]


class Solution3:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(c for c in s.lower() if c.isalnum())
        for i in range((len(new_s) // 2)+1):
            print(i, -1-i)
            print(new_s[i], new_s[-1 - i])
            if new_s[i] != new_s[-1 - i]:
                return False
        return True
