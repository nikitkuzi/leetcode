class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        mnx = inf
        mny = inf
        mxx = 0
        mxy = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    mnx = min(x, mnx)
                    mny = min(y, mny)
                    mxx = max(x, mxx)
                    mxy = max(y, mxy)
        return (mxx - mnx + 1) * (mxy - mny + 1)