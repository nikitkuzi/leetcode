class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        cols = [0]*m
        rows = [0]*n
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cols[j] +=1
                    rows[i] +=1
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += (rows[i]-1)*(cols[j]-1)
        return ans