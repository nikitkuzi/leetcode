class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        water = []
        n = len(grid)
        m = len(grid[0])

        def check(x, y):
            return x >= 0 and y >= 0 and x < n and y < m

        moves = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        visited = [[0 for _ in range(m)] for _ in range(n)]
        area = [0] * (n * m)

        def bfs(x, y, curr):
            visited[x][y] = curr
            res = 0
            for dx, dy in moves:
                if check(x + dx, y + dy) and visited[x + dx][y + dy] == 0 and grid[x + dx][y + dy]:
                    res += bfs(x + dx, y + dy, curr)
            # visited[x][y] = curr
            return res + 1

        cnt = 1
        islands = [0]
        # for g in grid:
        # print(g)
        # print()
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 0:
                    water.append((x, y))
                else:
                    if visited[x][y] == 0:
                        islands.append(bfs(x, y, cnt))
                        cnt += 1
        mx = 0
        # for v in visited:
        # print(v)
        # print(islands)
        for x, y in water:
            nghb = set()
            for dx, dy in moves:
                if check(x + dx, y + dy) and visited[x + dx][y + dy]:
                    nghb.add(visited[x + dx][y + dy])
            sm = 1
            for isl in nghb:
                sm += islands[isl]
            mx = max(sm, mx)
        return mx if mx else n * m

