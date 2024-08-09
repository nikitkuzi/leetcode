class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0
        for i in range(n - 2):
            for j in range(m - 2):
                s = set([grid[k][z] for k in range(i, i + 3) for z in range(j, j + 3)])

                r1 = sum(grid[i][j:j + 3])
                r2 = sum(grid[i + 1][j:j + 3])
                r3 = sum(grid[i + 2][j:j + 3])
                if r1 != r2 or r2 != r3 or len(s) != 9:
                    continue
                c1 = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                c2 = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
                # print(c1,c2)
                c3 = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]
                if c1 != c2 or c2 != c3:
                    continue
                d1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                d2 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
                if r1 == r2 and r2 == r3 and r3 == c1 and c1 == c2 and c2 == c3 and c3 == d1 and d1 == d2:
                    res += 1
        return res
