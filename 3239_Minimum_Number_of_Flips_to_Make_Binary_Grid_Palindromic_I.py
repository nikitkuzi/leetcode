class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        diff_row = 0
        diff_col = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m // 2):
                if grid[i][j] != grid[i][m - j - 1]:
                    diff_row += 1
                # if grid[i][j] != grid[n-i-1][j]:
                #     diff_col += 1

        for i in range(n // 2):
            for j in range(m):
                if grid[i][j] != grid[n - i - 1][j]:
                    diff_col += 1

        # if m % 2 == 1:
        #     for i in range(n):
        #         if grid[i][m//2] != grid[n-i-1][m//2]:
        #             diff_col += 1
        # print(diff_col,)
        return min(diff_col, diff_row)


