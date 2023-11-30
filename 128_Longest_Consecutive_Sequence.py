from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = defaultdict(bool)
        d = defaultdict(list)
        max_len = 0
        for num in nums:
            if num in seen:
                continue
            seen[num] = True
            l, r = num,num
            if d[num + 1]:
                r = d[num + 1][0]
            if d[num - 1]:
                l = d[num - 1][1]
            d[r] = [r, l]
            d[l] = [r, l]
            max_len = max(max_len, r - l + 1)
        return max_len


test = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(test.longestConsecutive(nums))
