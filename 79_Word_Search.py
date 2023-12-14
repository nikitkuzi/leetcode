class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1

        # Count number of letters in word
        # Check if board has all the letters in the word and they are atleast same count from word
        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False
        def check(x, y):
            nonlocal m
            nonlocal n
            return x >= 0 and x < m and y >= 0 and y < n
        ans = False
        def f(x, y, k):
            # print(x,y,board[x][y],k)
            char = board[x][y]
            if k == len(word):
                nonlocal ans
                ans = True
                return
            board[x][y] = '.'
            for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                if check(x+dx,y+dy) and board[x+dx][y+dy] == word[k]:
                    f(x+dx,y+dy, k+1)
            board[x][y] = char
        for x in range(m):
            for y in range(n):
                if word[0] == board[x][y]:
                    f(x,y,1)
        return ans
