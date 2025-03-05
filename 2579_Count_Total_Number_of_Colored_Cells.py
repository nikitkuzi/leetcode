class Solution:
    def coloredCells(self, n: int) -> int:
        return n*n*2-2*n+1
        if n == 1:
            return 1
        if n == 2:
            return 5
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 5
        for i in range(3,n+1):
            dp[i] = dp[i-1]+4+(i-2)*4
        return dp[n]