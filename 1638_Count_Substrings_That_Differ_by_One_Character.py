class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        dp = [[[0, 0] for _ in range(len(t) + 1)] for i in range(len(s) + 1)]
        ans = 0
        for i in range(1, len(s) + 1):
            dp[i][1][1] = (s[i - 1] == t[0]) ^ 1
        for j in range(1, len(t) + 1):
            dp[1][j][1] = (s[0] == t[j - 1]) ^ 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j][0] = dp[i - 1][j - 1][0] + 1
                    dp[i][j][1] = dp[i - 1][j - 1][1]

                else:
                    dp[i][j][0] = 0
                    # dp[i][j][1] = max(dp[i-1][j-1][0], dp[i-1][j][0],dp[i][j-1][0])
                    dp[i][j][1] = dp[i - 1][j - 1][0] + 1
                ans += dp[i][j][1]
        # for d in dp:
        # print(d)
        return ans
