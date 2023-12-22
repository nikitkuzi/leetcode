class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        if nums[0] < nums[-1]:
            return nums[0]
        first = True
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid

        return nums[l]
