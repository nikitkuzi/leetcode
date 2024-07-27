class Solution:
    def minChanges(self, n: int, k: int) -> int:
        res = 0
        while k:
            if k & 1 != n & 1:
                if k & 1 == 1:
                    return -1
                else:
                    res += 1
            k >>= 1
            n >>= 1
            # print(k,n)
        while n:
            res += int(n & 1)
            n >>= 1
        return res
