import heapq

class MedianFinder:
    def __init__(self):
        self.left, self.right = [], [] # max heap, min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        # all letf < right
        if (self.left and self.right and -self.left[0] > self.right[0]):
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # uneven size
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]

        return (-self.left[0] + self.right[0])/2

class MedianFinder2:
    def __init__(self):
        self.min_heap = []  # To store the larger half of numbers
        self.max_heap = []  # To store the smaller half of numbers

    def addNum(self, num: int) -> None:
        # Push the number to the max-heap (negated) to simulate a min-heap
        heapq.heappush(self.max_heap, -num)

        # Pop the smallest number from the max-heap and push it to the min-heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # If the min-heap has more elements than the max-heap, balance the heaps
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # If the total count of numbers is odd, the median is the top of the max-heap
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]

        # If the total count of numbers is even, the median is the average of the tops of both heaps
        return (-self.max_heap[0] + self.min_heap[0]) / 2

