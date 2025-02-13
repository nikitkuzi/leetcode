class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        mn = nums[0]
        res = 0
        n = len(nums)
        if mn >= k:
            return 0
        while nums:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            res += 1
            new = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new)
            if nums[0] >= k:
                return res
