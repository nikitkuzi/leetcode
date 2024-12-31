class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            for j in range(m):
                if grid[i][j] <= grid[i-1][j]:
                    res += grid[i-1][j] - grid[i][j] + 1
                    grid[i][j] = grid[i-1][j] + 1
        return res