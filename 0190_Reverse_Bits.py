class Solution:
    def reverseBits(self, n: int) -> int:
        ret_str = ""
        while n:
            ret_str += str(n & 1)
            n = n >> 1
        ret_str += "0" * (32 - len(ret_str))
        return int(ret_str, 2)

    def reverseBits2(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
