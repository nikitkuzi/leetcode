class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        ans = 0
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def in_boundaries(x, y):
            return x >= 0 and x < n and y >= 0 and y < m

        def bfs(x, y):
            if visited[x][y]:
                return
            visited[x][y] = 1
            for dx, dy in moves:
                if in_boundaries(x + dx, y + dy) and grid[x][y] == '1':
                    bfs(x + dx, y + dy)

        for x in range(n):
            for y in range(m):
                if not visited[x][y] and grid[x][y] == '1':
                    bfs(x, y)
                    ans += 1
        return ans
