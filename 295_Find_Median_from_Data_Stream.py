class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right and self.right[0] < num:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        if len(self.left) > len(self.right):
            heapq.heappush(self.right, -heapq.heappop(self.left))
        # print(self.left,self.right)

    def findMedian(self) -> float:
        if (len(self.right) + len(self.left)) % 2:
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2





