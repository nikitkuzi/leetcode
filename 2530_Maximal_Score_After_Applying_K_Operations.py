class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)
        score = 0
        for i in range(k):
            curr = heapq.heappop(h)
            score += -curr
            curr = (-curr+2)//3
            heapq.heappush(h, -curr)
        return score