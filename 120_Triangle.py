class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j == 0:
                    prev = triangle[i-1][j]
                elif j == i:
                    prev = triangle[i-1][j-1]
                else:
                    prev = min(triangle[i-1][j],triangle[i-1][j-1])
                triangle[i][j] = triangle[i][j] + prev

        return min(triangle[-1])