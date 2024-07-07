class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if colors[i] != colors[i - 1]:
                dp[i] = dp[i - 1] + 1
        for i in range(k - 1, n):
            # if dp[i]-dp[i-k+1] > 0:
            if dp[i] - k + 1 >= 0:
                res += 1

        # print(dp)
        if colors[0] == colors[-1]:
            return res
        dp[0] = dp[-1] + 1
        if dp[0] - k + 1 >= 0:
            res += 1
        for i in range(1, k - 1):
            if dp[i]:
                dp[i] = dp[i - 1] + 1
            # if dp[i] - dp[-k+i+1] > 0:
            if dp[i] - k + 1 >= 0:
                res += 1
        # print(dp)
        return res
