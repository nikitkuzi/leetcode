class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        ans = inf
        @cache
        def f(curr, ind):
            curr = sorted(curr)
            if ind==n:
                nonlocal ans
                ans = min(ans, max(curr))
                return
            for j in range(k):
                curr[j]+=cookies[ind]
                f(tuple(curr), ind+1)
                curr[j]-=cookies[ind]
        f(tuple([0]*k), 0)
        return ans