class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        # print(nums)
        for i, n in enumerate(nums):
            if n > upper:
                return res
            else:
                pos_left = bisect.bisect_left(nums, lower-n, i+1)
                pos_right = bisect.bisect_right(nums, upper-n, i+1)
                # print(n, i, pos_left, pos_right)
                res += pos_right - pos_left
        return res