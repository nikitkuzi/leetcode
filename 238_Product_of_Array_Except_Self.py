class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        sol = [1] * length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre * nums[i]
            sol[length - i - 1] *= post
            post = post * nums[length - i - 1]
            print(sol)
        return (sol)

test = Solution()
nums = [1,2,3,4]
print(test.productExceptSelf(nums))