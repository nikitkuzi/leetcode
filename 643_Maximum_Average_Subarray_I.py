class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(0, len(nums) - k):
            next_sum = cur_sum + nums[k + i] - nums[i]
            if next_sum > max_sum:
                max_sum = next_sum
            cur_sum = next_sum
        return max_sum / k