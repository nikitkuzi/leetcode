class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:]
        heapq.heapify(h)
        for _ in range(len(nums)-k):
            heapq.heappop(h)
        return h[0]