class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        s, m, n = 0, len(grid), len(grid[0])
        grid = [x + [0] for x in grid] + [[0] * n]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    s += 4 - 2 * (grid[row + 1][col] + grid[row][col + 1])
        return s