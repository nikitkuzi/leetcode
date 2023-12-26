from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        m = defaultdict(int)
        
        for num in nums:
            m[num] += 1
        
        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0


test = Solution()
nums = [3,2,3]
print(test.majorityElement(nums))