class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0]*24
        def f(num):
            i = 0
            while num:
                bits[23-i] += num & 1
                num >>=1
                i+=1
        for n in candidates:
            f(n)
        return max(bits)