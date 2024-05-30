class Solution:
    def twoEggDrop(self, n: int) -> int:
        k = 2
        dp = [[0 for _ in range(k+1)] for i in range(1000)]
        m = 0
        while dp[m][k] < n:
            m+=1
            for i in range(1, k+1):
                dp[m][i] = dp[m-1][i-1]+dp[m-1][i]+1
        return m
