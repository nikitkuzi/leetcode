class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zeroes_x = set()
        zeroes_y = set()
        n = len(matrix[0])
        m = len(matrix)
        for x in range(m):
            # if x in zeroes_x:
                # continue
            for y in range(n):
                # if y in zeroes_y:
                    # continue
                if matrix[x][y] == 0:
                    zeroes_x.add(x)
                    zeroes_y.add(y)
        print(zeroes_x, zeroes_y)
        for x in zeroes_x:
            for i in range(n):
                matrix[x][i] = 0
        for y in zeroes_y:
            for i in range(m):
                matrix[i][y] = 0

        print(matrix)


test = Solution()

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
test.setZeroes(matrix)
