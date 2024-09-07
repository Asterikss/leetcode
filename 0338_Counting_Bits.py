from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0]

        for n in range(1, n + 1):
            ones = 0
            while n > 0:
                ones += n&1
                n = n >> 1

            counts.append(ones)

        return counts

    def countBits2(self, n: int) -> List[int]:
        counts = [0] * (n + 1)

        for i, n in enumerate(range(1, n + 1), 1):
            ones = 0
            while n > 0:
                ones += n&1
                n = n >> 1

            counts[i] = ones

        return counts

    def countBits3(self, n: int) -> List[int]:
        counts = [0] * (n + 1)
        current_power_of_two = 1

        for n in range(1, n + 1):
            if current_power_of_two * 2 == n:
                current_power_of_two = n
            counts[n] = 1 + counts[n - current_power_of_two]
            
        return counts

        
    # 1 % 2 - 1
    # 2 - 0
    # 3 - 1

    # 11111
    # and
    # 01101
        
    #     000

    #       1 1

    #      10 1
    #      11 2

    #     100 1
    #     101 2
    #     110 2
    #     111 3

    #    1000 1
    #    1001 2
    #    1010 2
    #    1011 3
    #    1100 2
    #    1101 3
    #    1110 3
    #    1111 4
