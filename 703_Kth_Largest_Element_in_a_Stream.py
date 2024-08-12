class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.kn = k
        heapq.heapify(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return heapq.nlargest( self.kn, self.heap)[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)