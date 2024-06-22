class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                res += 1
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
        return res if sum(nums[-3:]) == 3 else -1
