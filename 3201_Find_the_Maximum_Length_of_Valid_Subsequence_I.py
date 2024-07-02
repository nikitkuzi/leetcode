class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = nums[0] % 2
        odd = 0
        even = 0
        both = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            if num % 2 == c:
                both += 1
                c = 1 - c

        return max(even, odd, both)