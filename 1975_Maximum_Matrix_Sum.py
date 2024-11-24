class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])
        neg = 0
        sm = 0
        mn = inf
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] < 0:
                    neg += 1
                mn = min(mn, abs(matrix[i][j]))
                res += abs(matrix[i][j])
        if neg % 2:
            res -= mn * 2
        return res
