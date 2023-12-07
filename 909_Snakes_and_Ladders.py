class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # board.reverse()
        n = len(board)
        self.mn = n ** 2 + 10

        # nums = [[j for j in range(1+i*n,(i+1)*n+1)] for i in range(n)]
        # for i in range(n):
        #     if i%2:
        #         nums[i].reverse()
        def get_idx(num):
            # x = (num-1) // n
            # y = n-1-((num-1) % n) if x%2 else (num-1) % n
            # return (x,y)
            r, c = divmod(num - 1, n)
            if r % 2 == 0:
                return n - 1 - r, c
            else:
                return n - 1 - r, n - 1 - c

        def get_moves(curr):
            return list(range(curr + 1, min(curr + 6, n ** 2) + 1))

        visited = [False] * (n ** 2)
        visited[0] = True
        q = deque()
        q.append((1, False, 0))

        while q:
            curr, jumped, cnt = q.popleft()
            x, y = get_idx(curr)
            if curr == (n ** 2):
                self.mn = min(self.mn, cnt)

            # visited[curr-1] = True
            # moves = get_moves(curr)
            for move in range(curr + 1, min(curr + 6, n ** 2) + 1):
                dx, dy = get_idx(move)
                # print(curr,move,board[dx][dy],cnt, jumped)
                # print(visited)
                if not visited[move - 1]:
                    next = board[dx][dy]
                    if next != -1:
                        # bfs(next,visited,True,cnt+1)
                        q.append((next, True, cnt + 1))
                    else:
                        # bfs(move,visited,False,cnt+1)
                        q.append((move, False, cnt + 1))
                    visited[move - 1] = True

        # print(board)
        # print(nums)
        if self.mn > n ** 2:
            return -1
        return self.mn




