class Solution:
    def clearStars(self, s: str) -> str:
        ans = ""
        heap = []
        deleted = set()
        for i,c in enumerate(s):
            if  c=='*':
                _, idx = heapq.heappop(heap)
                deleted.add(i)
                deleted.add(-idx)
            else:
                heapq.heappush(heap, (ord(c),-i))
        for i in range(len(s)):
            if i not in deleted:
                ans+=s[i]
        return ans
