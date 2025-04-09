class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        seen = set()
        for n in nums:
            if n < k:
                return -1
            else:
                if n not in seen and n != k:
                    res+=1
                    seen.add(n)
        return res