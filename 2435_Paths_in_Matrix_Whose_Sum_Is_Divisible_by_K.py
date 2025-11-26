class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(grid)
        m = len(grid[0])
        dp = [[[0 for i in range(k)] for j in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(1, n):
            for t in range(k):
                rem = grid[i][0] % k
                if dp[i - 1][0][t]:
                    dp[i][0][(t + rem) % k] = 1
        for j in range(1, m):
            for t in range(k):
                rem = grid[0][j] % k
                if dp[0][j - 1][t]:
                    dp[0][j][(t + rem) % k] = 1

        for i in range(1, n):
            for j in range(1, m):
                rem = grid[i][j] % k
                for t in range(k):
                    if dp[i - 1][j][t]:
                        dp[i][j][(t + rem) % k] += dp[i - 1][j][t]
                    if dp[i][j - 1][t]:
                        dp[i][j][(t + rem) % k] += dp[i][j - 1][t]
                    dp[i][j][(t + rem) % k] %= MOD

        # for d in dp:
        #     for i, t in enumerate(d):
        #         print(t, end = ' ')
        #     print()
        return dp[-1][-1][0]