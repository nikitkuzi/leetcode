class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)+1
        m=[[] for _ in range(n)]
        for i,j in edges:
            m[i].append(j)
            m[j].append(i)
        def cost(i):
            return 2-(i%2)
        @lru_cache(None)
        def dp(i,prev):
            res=0
            for j in m[i]:
                if j==prev: continue
                res=max(res, dp(j,i))
            return res + cost(i)
        res=[0]*n
        def dp2(i,prev,an):
            a,b = (-1,an),(-2,0)
            for j in m[i]:
                if j==prev: continue
                v = dp(j, i)
                if v>a[1]: a,b = (j,v), a
                elif v>b[1]: b = (j,v)
            res[i] = a[1]
            for j in m[i]:
                if j==prev: continue
                if j==a[0]: dp2(j, i, b[1] + cost(i))
                else: dp2(j, i, a[1] + cost(i))
        dp2(0,0,0)
        return res