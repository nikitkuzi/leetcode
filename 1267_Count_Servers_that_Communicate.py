class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        cols = [0] * m
        rows = [0] * n
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
                    # res+=1
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if rows[i] > 1 or cols[j] > 1:
                        res += 1

        return res