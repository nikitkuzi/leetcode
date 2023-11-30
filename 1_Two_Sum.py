from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = defaultdict(int)
        for i, num in enumerate(nums):

            print(d)
            if (target-num) in d:
                return [d[target-num], i]
            d[num] = i


test = Solution()
# nums = [2, 7, 11, 15]
# target = 9
nums = [3,2,4]
target = 6

print(test.twoSum(nums, target))
