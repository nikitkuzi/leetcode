class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        mx = 0
        # for i in matrix:
        # print(i)
        # print()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = int(matrix[i][j]) if (int(matrix[i - 1][j - 1]) + int(matrix[i - 1][j]) + int(
                        matrix[i][j - 1]) + int(matrix[i][j])) < 4 else min(int(dp[i - 1][j - 1]), int(dp[i - 1][j]),
                                                                            int(dp[i][j - 1])) + 1
                mx = max(mx, dp[i][j])
        # for i in dp:
        # print(i)
        return mx ** 2
