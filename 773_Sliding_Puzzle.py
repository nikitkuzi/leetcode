class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited = set()
        q = deque()
        state = tuple(map(tuple, board))
        q.append((state, 0))
        target_state = ((1,2,3), (4,5,0))
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def check(x,y):
            return x >= 0 and x < 2 and y>= 0 and y < 3
        def find_zero(state):
            for i in range(2):
                for j in range(3):
                    if state[i][j] == 0:
                        return i,j
        while q:
            state, res = q.popleft()
            # print(state, res)
            # print(type(state))
            if state in visited:
                continue
            else:
                visited.add(state)
            if state == target_state:
                return res
            x,y = find_zero(state)
            for dx, dy in moves:
                if check(x+dx, y+dy):
                    temp = list(map(list, state))
                    temp[x][y], temp[x+dx][y+dy] = temp[x+dx][y+dy], temp[x][y]
                    q.append((tuple(map(tuple, temp)), res+1))
        return -1