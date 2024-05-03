class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mid = n//2
        median = nums[mid]
        if median < k:
            return sum(k - num for num in nums[mid:n]  if num < k)
        if median > k:
            return sum(num - k for num in nums[:mid+1] if num > k)
        return 0