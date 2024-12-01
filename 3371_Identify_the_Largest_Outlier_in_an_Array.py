class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        sm = sum(nums)
        mx = -inf
        nums = Counter(nums)
        for outlier in nums.keys():
            rem = sm - outlier
            if rem % 2:
                continue
            rem //= 2
            if rem in nums:
                if rem == outlier and nums[rem] <= 1:
                    continue
                else:
                    mx = max(mx, outlier)

        return mx