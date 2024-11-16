class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        cumulative_sum = 1
        res = [-1 ] * (len(nums) - k + 1)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cumulative_sum += 1
                if cumulative_sum >= k:
                    res[i - k + 1]=nums[i]
            else:
                cumulative_sum = 1
        return res