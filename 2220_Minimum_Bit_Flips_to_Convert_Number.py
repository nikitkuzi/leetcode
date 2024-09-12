class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        while goal or start:
            res += ((start & 1) ^ (goal & 1))
            goal >>= 1
            start >>=1
        return res