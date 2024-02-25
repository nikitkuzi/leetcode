# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = 1
#         for i in range(1,n):
#             dp[0][i] = dp[0][i-1]
#         for i in range(1,m):
#             dp[i][0] = dp[i-1][0]
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j] = dp[i-1][j]+dp[i][j-1]
#         return dp[-1][-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] + [0] * (n - 1)

        for _ in range(m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[-1]