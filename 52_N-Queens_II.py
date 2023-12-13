class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = [0 for _ in range(n)]
        ldiag = [0 for _ in range(n * 2 + 1)]
        rdiag = [0 for _ in range(n * 2 + 1)]
        ans = 0

        def f(k):
            nonlocal rows
            nonlocal ldiag
            nonlocal rdiag
            nonlocal ans

            for i in range(n):
                r = i+k
                l = k-i+n-1
                if not rows[i] and not ldiag[l] and not rdiag[r]:
                    if k+1 == n:
                        ans+=1
                    rows[i]=1
                    ldiag[l] = 1
                    rdiag[r] = 1
                    f(k+1)
                    rows[i] = 0
                    ldiag[l] = 0
                    rdiag[r] = 0
        f(0)
        # ans*=2
        # No optimization for symmetry
        print(ans)
        return ans
test = Solution()
test.totalNQueens(2)

assert test.totalNQueens(1) == 1
assert test.totalNQueens(2) == 0
assert test.totalNQueens(3) == 0
assert test.totalNQueens(4) == 2
assert test.totalNQueens(5) == 10
assert test.totalNQueens(6) == 4
assert test.totalNQueens(7) == 40
