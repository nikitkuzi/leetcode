class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        for n in nums:
            if n in seen:
                ans ^= n
            else:
                seen.add(n)
        return ans