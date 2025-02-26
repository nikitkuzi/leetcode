class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr = 0
        cur = 0
        mx = -inf
        for n in nums:
            curr = max(curr+n, n)
            cur = min(cur+n, n)
            mx = max(mx, abs(curr), abs(cur))
        return mx