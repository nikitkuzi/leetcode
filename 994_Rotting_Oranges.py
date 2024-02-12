class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def in_boundaries(x, y):
            return x >= 0 and y >= 0 and x < n and y < m

        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        q = deque()
        cnt = 0
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                for dx, dy in moves:
                    if in_boundaries(x + dx, y + dy) and grid[x + dx][y + dy] == 1:
                        q.append([x + dx, y + dy])
                        grid[x + dx][y + dy] = 2
                        fresh -= 1
            cnt += 1
        return -1 if fresh else cnt
