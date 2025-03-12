class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        zer_l = bisect_left(nums, 0)
        zer_r = bisect_right(nums, 0)
        # print(neg)
        return max(zer_l, len(nums)-zer_r)