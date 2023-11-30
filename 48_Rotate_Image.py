class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # n = len(matrix) - 1
        # for i in range((n + 1) // 2):
        #     for j in range(i, n - i):
        #         matrix[i][j], matrix[n - j][i], matrix[n - i][n - j], matrix[j][n-i] = matrix[n - j][i], matrix[n-i][n-j], matrix[j][n - i],matrix[i][j]
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        print(matrix)

test = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test.rotate(matrix)
