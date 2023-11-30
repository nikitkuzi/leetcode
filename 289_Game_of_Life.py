class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        n = len(board[0])
        m = len(board)
        state = [[0]*n for _ in range(m)]
        # print(board)
        # print(state)
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        dead = 0
        live = 0

        def in_bountaries(self, x, y):
            return (x >= 0) and (x < m) and (y >= 0) and (y < n)

        for i in range(m):
            for j in range(n):
                for x, y in direction:
                    if in_bountaries(self, i + x, j + y) and board[i + x][j + y] == 0:
                        dead += 1
                    if in_bountaries(self, i + x, j + y) and board[i + x][j + y] == 1:
                        live += 1
                if board[i][j] == 0 and live == 3:
                    state[i][j] = 1
                elif board[i][j] == 1 and live < 2:
                    state[i][j] = 0
                elif board[i][j] == 1 and 2 <= live <= 3:
                    state[i][j] = board[i][j]
                elif board[i][j] == 1 and live > 3:
                    state[i][j] = 0
                # print(dead, live, board[i][j], state[i][j])
                dead = 0
                live = 0
        for i in range(m):
            for j in range(n):
                board[i][j] = state[i][j]
        print(board)



test = Solution()

board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
test.gameOfLife(board)
