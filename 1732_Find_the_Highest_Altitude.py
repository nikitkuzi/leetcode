class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        cur = 0
        for n in gain:
            cur+=n
            if mx<cur:
                mx = cur
        return mx