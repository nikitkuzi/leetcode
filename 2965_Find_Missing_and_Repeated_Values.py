class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = [0, 0]
        seen = set()
        sm = 0
        n = len(grid)
        for x in range(n):
            for y in range(n):
                if grid[x][y] in seen:
                    res[0] = (grid[x][y])
                else:
                    sm += grid[x][y]
                    seen.add(grid[x][y])
        res[1] = int((1 + n ** 2) / 2 * n ** 2 - sm)
        return res
