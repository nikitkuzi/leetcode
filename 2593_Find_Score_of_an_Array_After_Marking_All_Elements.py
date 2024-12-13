class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False]*len(nums)
        score = 0
        h = []
        for i, n in enumerate(nums):
            heapq.heappush(h, (n, i))
        while h:
            n, i = heapq.heappop(h)
            if not marked[i]:
                score += n
                marked[i] = True
                if i > 0:
                    marked[i-1] = True
                if i < len(nums)-1:
                    marked[i+1] = True
        return score