class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        n = len(isWater)
        m = len(isWater[0])
        visited = [[-1 for i in range(m)] for j in range(n)]
        for x in range(n):
            for y in range(m):
                if isWater[x][y]:
                    q.append((x, y, 0))
                    visited[x][y] = 0
        moves = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        def check(x, y):
            return x >= 0 and y >= 0 and x < n and y < m
        while q:
            x, y, h = q.popleft()
            for dx, dy in moves:
                if check(x+dx, y+dy):
                    if visited[x+dx][y+dy] == -1:
                        visited[x+dx][y+dy] = h+1
                        q.append((x+dx, y+dy, h+1))
        return visited