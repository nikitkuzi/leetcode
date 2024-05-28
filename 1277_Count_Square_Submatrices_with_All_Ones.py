class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    if i==0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                ans+=dp[i][j]
        # for d in dp:
            # print(d)
        return ans