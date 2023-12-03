class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        visited = [[0 for a in range(m)] for _ in range(n)]
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def check(x, y):
            return x >= 0 and x < n and y >= 0 and y < m

        def bfs(x, y):
            if visited[x][y]:
                return

            visited[x][y] = 1
            for dx, dy in moves:
                if check(x + dx, y + dy) and board[x + dx][y + dy] == 'O':
                    bfs(x + dx, y + dy)

        for x in range(n):

            if not visited[x][0] and board[x][0] == 'O':
                bfs(x, 0)
            if not visited[x][m - 1] and board[x][m - 1] == 'O':
                bfs(x, m - 1)
        for y in range(m):

            if not visited[0][y] and board[0][y] == 'O':
                bfs(0, y)
            if not visited[n - 1][y] and board[n - 1][y] == 'O':
                bfs(n - 1, y)
        for x in range(n):
            for y in range(m):
                if not visited[x][y]:
                    board[x][y] = 'X'




