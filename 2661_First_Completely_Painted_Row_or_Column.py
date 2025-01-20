class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [0]*n
        cols = [0]*m
        matrix = [0]*(m*n+1)
        for i in range(n):
            for j in range(m):
                matrix[mat[i][j]] = (i, j)
        # for i in range(len(arr)):
        for i in range(len(arr)):
            x, y = matrix[arr[i]]
            rows[x]+=1
            cols[y]+=1
            # print(rows)
            # print(cols)
            # print()
            if rows[x] == m or cols[y] == n:
                return i
        # return 0
