class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        parents = [i for i in range(n * m)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def find(x, y):
            if parents[x * n + y] != x * n + y:
                return find(parents[x * n + y])
            return parents[x * n + y]

        # def union(x1, y1, x2, y2):
        def union(x1, y1, parent):
            p1 = find(x1, y1)
            # p2 = find(x2, y2)
            parents[p1] = parent

        def check(x, y):
            if x < 0 or y < 0 or x >= n or y >= m:
                return False
            return True

        def f(x, y, parent):
            for dx, dy in moves:
                if check(x + dx, y + dy) and grid1[x + dx][y + dy] != 0 and parents[(x + dx) * n + y + dy] == (
                        x + dx) * n + y + dy:
                    union(x + dx, y + dy, parent)
                    f(x + dx, y + dy, parent)

        for x in range(n):
            for y in range(m):
                if grid1[x][y] != 0 and parents[x * n + y] == x * n + y:
                    f(x, y, x * n + y)

        for i in range(n):
            for j in range(m):
                print(parents[i * n + j], end=' ')
            print()