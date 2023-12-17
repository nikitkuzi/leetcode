class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if target < nums[0]:
            return 0
        # mid = (l+r)//2
        while l <= r:

            mid = (l + r) // 2
            # print(mid,nums[mid],target)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        # print(mid,nums[mid],target)
        # print(mid)
        return l
