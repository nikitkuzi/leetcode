class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        g = [[0] * n for i in range(n)]
        for x1, y1, x2, y2 in queries:
            for i in range(x1, x2 + 1):
                g[i][y1] += 1
                if y2 + 1 < n:
                    g[i][y2 + 1] -= 1

        for i in range(n):
            for j in range(1, n):
                g[i][j] += g[i][j - 1]
        return g