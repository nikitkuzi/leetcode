class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        curr_total = 0
        min_len = len(nums) + 1
        for r in range(len(nums)):
            curr_total += nums[r]
            if curr_total >= target:
                while curr_total - nums[l] >= target:
                    curr_total -= nums[l]
                    l += 1
                if r - l + 1 < min_len:
                    min_len = r - l + 1
        return min_len if min_len < len(nums) + 1 else 0

test = Solution()
target = 7
nums = [2, 3, 1, 2, 4, 3, 3, 1, 3, 1, 1]
# target = 7
# nums = [2,3,1,2,4,3]
# target = 4
# nums = [1,4,4]
# target = 11
# nums = [1,1,1,1,1,1,1,1]
# target = 11
# nums = [1,2,3,4,5]

print(test.minSubArrayLen(target, nums))
