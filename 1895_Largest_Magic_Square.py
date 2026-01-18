# class Solution:
#     def largestMagicSquare(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#         r = [[0 for i in range(m+1)] for j in range(n)]
#         c = [[0 for j in range(n+1)] for i in range(m)]
#         def md(x,y,side):
#             sm = 0
#             for dx in range(side):
#                 sm += grid[x-dx][y-dx]
#             return sm
#         def sd(x,y,side):
#             sm = 0
#             y = y - side + 1
#             for dx in range(side):
#                 sm += grid[x-dx][y+dx]
#             return sm

#         def check(x,y,side):
#             sm_r = r[x][y+1] - r[x][y+1-side]
#             sm_c = c[y][x+1] - c[y][x+1-side]
#             d1 = md(x,y,side)
#             d2 = sd(x,y,side)
#             # print(sm_r, sm_c, d1, d2)
#             if len(set([sm_r, sm_c, d1,d2]))!= 1:
#                 return False

#             if any(sm_r != r[i][y+1]-r[i][y+1-side] for i in range(x-side+1, x)):
#                 return False

#             if any(sm_c != c[i][x+1]-c[i][x+1-side] for i in range(y-side+1, y)):
#                 return False
#             return True

#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 r[i-1][j] = grid[i-1][j-1] + r[i-1][j-1]
#         for j in range(1, m+1):
#             for i in range(1, n+1):
#                 c[j-1][i] = grid[i-1][j-1] + c[j-1][i-1]
#         mx = 1

#         for side in range(2, min(m,n)+1):
#             for i in range(side-1, n):
#                 f = False
#                 for j in range(side-1, m):
#                     # print(i,j,side)
#                     if check(i,j,side):
#                         mx = side
#                         f = True
#                         break
#                 if f:
#                     break

#         return mx
from itertools import accumulate
from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # m = rows, n = cols

        # Row prefix sums
        # rs[r][c] = sum of grid[r][0..c-1]
        rs = [[0] + list(accumulate(row)) for row in grid]
        # Column prefix sums
        # cs[r][c] = sum of grid[0..r-1][c]
        cs = [[0] * n for _ in range(m + 1)]

        # Main diagonal prefix sums
        # ds[r][c] = sum along diagonal ending at (r-1, c-1)
        ds = [[0] * (n + 1) for _ in range(m + 1)]

        # Anti-diagonal prefix sums
        # ads[r][c] = sum along anti-diagonal ending at (r-1, c+1)
        ads = [[0] * (n + 1) for _ in range(m + 1)]

        # Build column, diagonal, anti-diagonal prefix arrays
        for r in range(m):
            for c in range(n):
                x = grid[r][c]
                cs[r + 1][c] = cs[r][c] + x
                ds[r + 1][c + 1] = ds[r][c] + x
                ads[r + 1][c] = ads[r][c + 1] + x

        # Try k x k square sizes from largest to smallest
        for k in range(min(m, n), 0, -1):
            # bottom-right corner of square in 1-based prefix space: (R, C)
            for R in range(k, m + 1):
                for C in range(k, n + 1):

                    # Main diagonal sum for this k × k square
                    diag_sum = ds[R][C] - ds[R - k][C - k]

                    # Anti-diagonal sum check
                    if ads[R][C - k] - ads[R - k][C] != diag_sum:
                        continue

                    # Check all row sums
                    # Row index in grid = r, row range = R-k .. R-1
                    if any(rs[r][C] - rs[r][C - k] != diag_sum for r in range(R - k, R)):
                        continue

                    # Check all column sums
                    # Column index in grid = c, column range = C-k .. C-1
                    if any(cs[R][c] - cs[R - k][c] != diag_sum for c in range(C - k, C)):
                        continue

                    return k  # Found largest valid square

        return 1  # At minimum, 1x1 squares are always magic

# Time = O(m n min(m, n)), Space = O(m n)