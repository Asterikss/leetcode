from collections import defaultdict, Counter
from typing import List
import heapq


class Solution:
    # 81ms Beats 90.14% | Memory 22.26 MB Beats 7.14% O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        helper_array = [[] for _ in range(len(nums))]
        for key, value in counter.items():
            helper_array[value-1].append(key)

        ret = []
        for keys_array in helper_array[::-1]:
            if keys_array:
                ret.extend(keys_array)
                if len(ret) >= k:
                    break

        return ret

    # Nice. Very fast too
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        return [tup[0] for tup in Counter(nums).most_common()[:k]]

    # nlogk (insertion and removal heap - logk; n elements to process)
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []

        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for _, num in heap]

    # nlogn
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        good_values = sorted([value for value in d.values()])[-k:]

        ret = []
        for key, value in d.items():
            if value in good_values:
                ret.append(key)

        return ret

# We can optimize it more by storing the maxFrequency while creating the HashMap
# (which has the integer and their corresponding frequency). Then, the next
# iteration to get the required elements can start from this maxFrequency
# instead of N.
