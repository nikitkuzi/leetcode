class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dp = [[0 for i in range(m)] for i in range(n)]
        dp[0][0] = moveTime[0][0]
        for j in range(1, m):
            dp[0][j] = max(dp[0][j-1]+1, moveTime[0][j]+1)
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0]+1, moveTime[i][0]+1)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(max(dp[i-1][j]+1, moveTime[i][j]+1), max(dp[i][j-1]+1, moveTime[i][j]+1))
        # for d in dp:
            # print(d)
        return dp[-1][-1]