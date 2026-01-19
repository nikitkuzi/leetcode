class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        l, r, ans = 1, min(m, n), 0
        while l <= r:
            mid = (l + r) // 2
            find = any(
                getRect(i, j, i + mid - 1, j + mid - 1) <= threshold
                for i in range(1, m - mid + 2)
                for j in range(1, n - mid + 2)
            )
            if find:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
# class Solution:
#     def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
#         n = len(mat)
#         m = len(mat[0])
#         mx = 0
#         r = [[0 for i in range(m+1)] for j in range(n)]
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 r[i-1][j] = mat[i-1][j-1] + r[i-1][j-1]
#                 if mat[i-1][j-1] <= threshold:
#                     mx = 1
#         for side in range(2, min(n,m)+1):
#             for x in range(side-1, n):
#                 f = False
#                 for j in range(side-1, m):
#                     sm = sum(r[i][j+1]-r[i][j+1-side] for i in range(x-side+1, x+1))
#                     if sm <= threshold:
#                         mx = side
#                         f = True
#                         break
#                 if f:
#                     break
#             if not f:
#                 return mx

#         return mx