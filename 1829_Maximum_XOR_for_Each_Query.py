class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = 0
        res = []
        for n in nums:
            mask ^= n
            last_bits = (((1<<maximumBit)-1) ^ mask)
            res.append(last_bits)
        return res[::-1]