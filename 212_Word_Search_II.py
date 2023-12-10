class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.used = False
        self.word = None


class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def build_trie(self, words: List[str]):
        for word in words:
            trie = self.root
            for c in word:
                trie = trie.children.setdefault(c, TrieNode())
            trie.is_word = True
            trie.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board[0])
        m = len(board)

        def check(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        # def dfs(x,y,trie):
        #     if trie.is_word and not trie.used:
        #         trie.used = True
        #         ans.append(trie.word)
        #     char = board[x][y]
        #     board[x][y] = 1
        #     neighbors = []
        #     for dx,dy in ([-1,0],[1,0],[0,1],[0,-1]):
        #         if check(x+dx,y+dy) and board[x+dx][y+dy] in trie.children:
        #             dfs(x+dx,y+dy,trie.children[board[x+dx][y+dy]])
        #             # neighbors.append((board[x+dx][y+dy],x+dx,y+dy))
        #     # for nghb,dx,dy in neighbors:
        #         # if nghb in trie.children:

        #             # print(nghb,"here")
        #             # dfs(dx,dy,trie.children[nghb])
        #     board[x][y] = char
        #     if not trie.children:
        #         trie = TrieNode()

        def dfs(x, y, trie):
            char = board[x][y]
            curr = trie[char]
            word = curr.pop("#", False)
            if word:
                ans.append(word)

            board[x][y] = 1
            neighbors = []
            for dx, dy in ([-1, 0], [1, 0], [0, 1], [0, -1]):
                if check(x + dx, y + dy) and board[x + dx][y + dy] in curr:
                    dfs(x + dx, y + dy, curr)
                    # neighbors.append((board[x+dx][y+dy],x+dx,y+dy))
            # for nghb,dx,dy in neighbors:
            # if nghb in trie.children:

            # print(nghb,"here")
            # dfs(dx,dy,trie.children[nghb])
            board[x][y] = char
            if not curr:
                trie.pop(char)

        self.build_trie(words)

        # trie = self.root

        trie = {}
        for word in words:
            curr = trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr["#"] = word

        ans = []
        for x in range(m):
            for y in range(n):
                # if board[x][y] in trie.children:
                # dfs(x,y, trie.children[board[x][y]])
                if board[x][y] in trie:
                    dfs(x, y, trie)
        return ans




