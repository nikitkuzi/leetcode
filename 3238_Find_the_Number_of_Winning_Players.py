class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        s = set()
        p = [[0 for i in range(11)] for _ in range(n)]
        for x,y in pick:
            p[x][y] += 1
            if p[x][y] > x:
                s.add(x)
        return len(s)
