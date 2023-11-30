class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ox, oy, x, y =  1, 0, 0, 0
        n = len(matrix[0])
        m = len(matrix)
        visited = 0
        ans = []
        d = 'r'
        while visited < n * m:
            if d == 'r':
                for i in range(n-oy):
                    if visited == n*m:
                        return ans
                    ans.append(matrix[x][y+i])
                    visited += 1
                d = 'd'
                y += (n - oy - 1)
                x += 1
                oy += 1

            if d == 'd':
                for i in range(m-ox):
                    if visited == n*m:
                        return ans
                    ans.append(matrix[x+i][y])
                    visited += 1
                d = 'l'
                x += m - ox - 1
                y -= 1
                ox += 1

            if d == 'l':
                for i in range(n-oy):
                    if visited == n*m:
                        return ans
                    ans.append(matrix[x][y-i])
                    visited += 1
                d = 'u'
                y -= (n - oy - 1)
                x -= 1
                oy += 1

            if d == 'u':
                for i in range(m - ox):
                    if visited == n*m:
                        return ans
                    ans.append(matrix[x-i][y])
                    visited += 1
                d = 'r'
                x -= (m - ox - 1)
                y += 1
                ox += 1
        return ans

    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     result = []
    #
    #     rowMin = 0
    #     rowMax = len(matrix) - 1
    #     colMin = 0
    #     colMax = len(matrix[0]) - 1
    #
    #     while rowMin <= rowMax and colMin <= colMax:
    #         for i in range(colMin, colMax + 1):
    #             result.append(matrix[rowMin][i])
    #
    #         for i in range(rowMin + 1, rowMax + 1):
    #             result.append(matrix[i][colMax])
    #
    #         if rowMin != rowMax:
    #             for i in range(colMax - 1, colMin - 1, -1):
    #                 result.append(matrix[rowMax][i])
    #
    #         if colMin != colMax:
    #             for i in range(rowMax - 1, rowMin, -1):
    #                 result.append(matrix[i][colMin])
    #
    #         rowMin += 1
    #         rowMax -= 1
    #         colMin += 1
    #         colMax -= 1
    #
    #     return result

test = Solution()
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[1,2,3,4, 5],[6,7,8,9,10],[11,12,13,14,15]]
matrix = [[1],[2,3,4]]
print(test.spiralOrder(matrix))