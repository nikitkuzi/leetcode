class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        count = 0
        while(n > 0):
            count = count + (n & 1)
            n >>= 1
        return count
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            res += (x&1)^(y&1)
            x>>=1
            y>>=1
        return res