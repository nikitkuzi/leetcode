class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result |= n&1
            result <<= 1
            n >>= 1
            # print(bin(result),bin(n))
        result >>= 1
        return result