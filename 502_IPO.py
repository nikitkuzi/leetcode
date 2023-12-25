class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        if w > max(capital):
            return w + sum(heapq.nlargest(k, profits))
        if w < min(capital):
            return w

        h = list(zip(capital, profits))
        heapq.heapify(h)
        valid_projs = []
        for _ in range(k):
            while h and h[0][0] <= w:
                # proj = heapq.heappop(h)
                # heapq.heappush(valid_projs, proj[1]*-1)
                heapq.heappush(valid_projs, -heapq.heappop(h)[1])

            if not valid_projs:
                return w

            # profit = heapq.heappop(valid_projs)
            # w += -profit
            w += -heapq.heappop(valid_projs)
        return w

