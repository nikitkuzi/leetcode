class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x =inf
        y = inf
        for row in ops:
            x = min(x, row[0])
            y = min(y, row[1])
        return m*n if not ops else x*y