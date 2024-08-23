from math import inf


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        mx = 0
        pos = 0
        for j in range(m):
            dp[0][j] = points[0][j]
            if mx < dp[0][j]:
                mx = dp[0][j]
                pos = j
        for i in range(1, n):
            mx_curr = 0
            pos_curr = 0
            for j in range(m):
                dp[i][j] = mx + points[i][j] - abs(j - pos)
                if mx_curr < dp[i][j]:
                    mx_curr = dp[i][j]
                    pos_curr = j
            mx = mx_curr
            pos = pos_curr
        return max(dp[-1])

