class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        dp = [[0 for i in range(n)] for j in range(n)]
        dp[-1][0] = fruits[-1][0]
        dp[0][-1] = fruits[0][-1]
        res = fruits[0][0]
        for i in range(1, n - 1):
            res += fruits[i][i]
            k = n - i - 1 if i < n // 2 else i + 1
            for j in range(k, n):
                dp[j][i] = max(dp[j - 1][i - 1], dp[j][i - 1], dp[j + 1 if j < n - 1 else j][i - 1]) + fruits[j][i]
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1 if j < n - 1 else j]) + fruits[i][j]

        return res + dp[-1][-2] + dp[-2][-1] + fruits[-1][-1]

