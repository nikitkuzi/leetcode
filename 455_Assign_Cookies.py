class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        ans = 0
        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                i+=1
                ans+=1
            if i >= len(g) or (i < len(g) and s[-1] < g[i]):
                break
        return ans