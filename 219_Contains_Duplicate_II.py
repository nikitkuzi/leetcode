from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            if len(nums[i:i + 1 + k]) != len(set(nums[i:i + 1 + k])):
                return True
        return False


test = Solution()
nums = [1, 2, 3, 1]
k = 3
print(test.containsNearbyDuplicate(nums, k))
