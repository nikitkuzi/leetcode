class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i,n in enumerate(nums):
            if n:
                nums[i],nums[zero] = nums[zero],nums[i]
                zero +=1
        # print(nums)
