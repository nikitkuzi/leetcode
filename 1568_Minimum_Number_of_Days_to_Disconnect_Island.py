class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        edges = 0

        def check(x, y):
            if x < 0 or y < 0 or x >= n or y >= m:
                return False
            return True

        def check_sm(x, y):
            sm = 0
            for dx, dy in moves:
                if check(x + dx, y + dy) and grid[x + dx][y + dy] == 1:
                    sm += 1
            return sm

        def dfs(x, y):
            if check_sm(x, y) <= 1:
                nonlocal edges
                edges += 1
            grid[x][y] = 0
            for dx, dy in moves:
                if check(x + dx, y + dy) and grid[x + dx][y + dy] == 1:
                    dfs(x + dx, y + dy)

        for x in range(n):
            for y in range(m):
                if grid[x][y] != 0:
                    if check_sm(x, y) <= 1:
                        edges += 1
                    for dx, dy in moves:
                        if check(x + dx, y + dy) and grid[x + dx][y + dy] == 1:
                            islands += 1
                            if islands == 2:
                                return 0
                            dfs(x + dx, y + dy)
        if edges == 1:
            return 1
        else:
            return 2
