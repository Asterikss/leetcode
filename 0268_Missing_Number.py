from typing import List

class Solution:
    # O(1) mem O(n)
    def missingNumber(self, nums: List[int]) -> int:
            nums_xors = nums[0]
            for i in range(1, (len(nums))):
                nums_xors ^= nums[i]

            reference_list_xors = 0
            for i in range(1, len(nums) + 1):
                reference_list_xors ^= i

            return reference_list_xors ^ nums_xors

    def missingNumber2(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1) // 2) - sum(nums)

    def missingNumber3(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

    def missingNumber4(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res

    def missingNumber5(self, nums: List[int]) -> int:
        nums.sort()
        expected = 0
        for num in nums:
            if num != expected:
                return expected
            expected = num + 1

        return expected

    # lol
    def missingNumber6(self, nums: List[int]) -> int:
        max_number = 0
        tmp = 0b0
        for num in nums:
            print(tmp)
            tmp |= num
            if max_number < num:
                max_number = num
            print(tmp)
        print(tmp)

        print(bin(max_number))
        print(bin(tmp))
        tmp_copm = tmp
        msb = 0
        while tmp:
            msb = 1
            tmp >>= tmp
        print("msb", msb)
        biggest_single_bit_number = 2**msb
        print(biggest_single_bit_number)
        all_ones_to_msb = 0
        while biggest_single_bit_number:
            all_ones_to_msb |= biggest_single_bit_number
            biggest_single_bit_number //= 2

        print(bin(all_ones_to_msb))
        #return 0
        print(bin(all_ones_to_msb ^ max_number))
        return all_ones_to_msb ^ max_number
