class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[k:] + nums[:k]
        print(nums)

test = Solution()
nums = [1, 2, 3, 4, 5, 6]
test.rotate(nums, k)