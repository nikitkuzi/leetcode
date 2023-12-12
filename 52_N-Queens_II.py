class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = [0 for _ in range(n)]
        ldiag = [0 for _ in range(n * 2 + 1)]
        rdiag = [0 for _ in range(n * 2 + 1)]
        ans = 0

        def f()

test = Solution()
test.totalNQueens(4)

assert test.totalNQueens(4) == 2
assert test.totalNQueens(1) == 1
