class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze[0])
        n = len(maze)
        maze[entrance[0]][entrance[1]] = '+'
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        def in_boundaries(x,y):
            return x >= 0 and x < n and y >=0 and y < m and maze[x][y] != '+'
        def check(x,y):
            return (x == 0 or y == 0 or x == n-1 or y == m-1) and [x,y]!=entrance

        q = deque()
        q.append([*entrance,0])

        while q:
            x,y,cnt = q.popleft()
            if check(x,y):
                return cnt
            for dx,dy in moves:
                if in_boundaries(x+dx,y+dy):
                    q.append((x+dx,y+dy,cnt+1))
                    maze[x+dx][y+dy] = '+'
        return -1
