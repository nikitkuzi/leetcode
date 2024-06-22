class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        swaps = 0
        for i in range(len(nums)):
            if swaps % 2 == 1:
                nums[i] ^= 1

            if nums[i] == 0:
                    swaps += 1
                    res += 1
        return res