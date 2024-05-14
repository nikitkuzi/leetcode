class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i < len(grid)-1 and grid[i][j] != grid[i+1][j]:
                    return False
                if j < len(grid[0])-1 and grid[i][j] == grid[i][j+1]:
                    return False
        return True