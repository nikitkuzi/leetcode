class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_len = nums[0]
        for i, element in enumerate(nums[1:-1], start=1):
            # print(i, element, max_len, i + element)
            if max_len >= i:
                max_len = max(max_len, i + element)
            # print(max_len)
        return True if max_len >= (len(nums) - 1) else False

test = Solution()
nums = [2,3,1,1,4]
print(test.canJump(nums))