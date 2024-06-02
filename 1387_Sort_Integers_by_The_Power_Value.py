class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def f(curr):
            if curr==1:
                return 0
            if curr%2==0:
                return f(curr//2)+1
            else:
                return f(curr*3+1)+1
        ans = []
        for n in range(lo, hi+1):
            ans.append((f(n),n))
        ans.sort()
        # print(ans)
        return ans[k-1][1]