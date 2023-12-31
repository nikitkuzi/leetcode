# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])

#         if m == 1 and n == 1:
#             return (obstacleGrid[0][0]+1)%2
#         if obstacleGrid[0][0] == 1:
#             return 0

#         obs = 1
#         for i in range(1,m):
#             if obstacleGrid[i][0] == 1:
#                 obs = -1
#             obstacleGrid[i][0] = obs
#         obs = 1
#         for i in range(1, n):
#             if obstacleGrid[0][i] == 1:
#                 obs = -1
#             obstacleGrid[0][i] = obs
#         obstacleGrid[0][0] = 1
#         for i in range(1,m):
#             for j in range(1,n):
#                 if obstacleGrid[i][j] == 1:
#                     obstacleGrid[i][j] = -1
#                 else:
#                     obstacleGrid[i][j] = max(0,obstacleGrid[i-1][j]) + max(0,obstacleGrid[i][j-1])
#         return max(obstacleGrid[-1][-1],0)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * COL
        dp[0] = 1

        for r in range(ROW):
            for c in range(COL):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                    continue
                if c > 0:
                    dp[c] += dp[c - 1]

        return dp[COL - 1]