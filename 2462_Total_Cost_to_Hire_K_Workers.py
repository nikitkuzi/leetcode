class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs)==1:
            return costs[0]
        if len(costs)//2<candidates:
            candidates = len(costs)//2
        l = candidates
        r = len(costs)-candidates-1
        left = costs[:candidates]
        right = costs[-candidates:]
        heapq.heapify(left)
        heapq.heapify(right)
        res = 0

        while l<=r and k>0:
            if left[0] <= right[0]:
                res += heapq.heappop(left)
                heapq.heappush(left,costs[l])
                l+=1
            else:
                res += heapq.heappop(right)
                heapq.heappush(right,costs[r])
                r-=1
            k-=1

        last = left + right
        heapq.heapify(last)
        while k>0:
            res+=heapq.heappop(last)
            k-=1
        return res