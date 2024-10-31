class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        moves = [[-1, 1], [0, 1], [1,1]]
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for i in range(m)] for i in range(n)]
        def check(x, y):
            return x >= 0 and x< n and y >= 0 and y < m
        for y in range(m-2, -1, -1):
            for x in range(n-1, -1, -1):
                curr = 0
                for dx, dy in moves:
                    if check(x+dx, y+dy) and grid[x][y] < grid[x+dx][y+dy]:
                        curr = max(dp[x+dx][y+dy]+1, curr)
                dp[x][y] = curr

        return max([dp[x][0] for x in range(n)])
