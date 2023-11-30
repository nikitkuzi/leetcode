from collections import Counter
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    # if [nums[i], nums[j], nums[k]] not in ans:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while k >= j and nums[j] == nums[j - 1]:
                        j += 1

        counts = Counter(nums)
        print(counts)
        result = [[0, 0, 0]] if counts[0] >= 3 else []
        nums = [i for i in sorted(counts) if i != 0]
        print(nums)
        return ans


test = Solution()
# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,1,1]
nums = [-1,0,1,2,-1,-4]

print(test.threeSum(nums))
