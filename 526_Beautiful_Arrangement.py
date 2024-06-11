class Solution:
    def countArrangement(self, n: int) -> int:
        num = [i+1 for i in range(n)]
        ans = 0
        def f(curr):
            if curr == n:
                nonlocal ans
                ans+=1
                # return
            for i in range(curr,n):
                if num[i]%(curr+1)==0 or (curr+1)%num[i]==0:
                    num[i],num[curr]=num[curr],num[i]
                    f(curr+1)
                    num[i],num[curr]=num[curr],num[i]
        f(0)
        return ans