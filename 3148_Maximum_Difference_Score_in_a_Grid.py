# class Solution:
#     def maxScore(self, grid: List[List[int]]) -> int:
#         dp = [[-inf for j in range(len(grid[0]))] for i in range(len(grid))]
#         n = len(grid)
#         m = len(grid[0])
#         for i in range(n):
#             for j in range(m):
#                 val = grid[i][j]

#                 # calculate max possible score from (i, j) by going rightwards
#                 if j >0:
#                     row_diff = val - grid[i][j-1]
#                     dp[i][j] = max(row_diff, row_diff + dp[i][j-1])

#                 # calculate max possible score from (i, j) by going downwards
#                 if i >0:
#                     col_diff = val - grid[i-1][j]
#                     dp[i][j] = max(dp[i][j], col_diff, col_diff + dp[i-1][j])
#         # print(dp)
#         return max(max(row) for row in dp)
class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        col = [inf] * len(grid[0])
        ans = -inf
        for row in grid:
            for i,n in enumerate(row):
                if i and col[i-1] < col[i]:
                    col[i] = col[i-1]
                if n - col[i] > ans:
                    ans = n - col[i]
                if n < col[i]:
                    col[i] = n
        return ans