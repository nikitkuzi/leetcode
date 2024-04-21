class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(x):
            if x == 1:
                return False
            for i in range(2, min(int(x**0.5) + 2, x)):
                if x % i == 0:
                    return False
            return True
        l = 0
        while l < len(nums):
            if isPrime(nums[l]):
                break
            l += 1
        r = len(nums) - 1
        while r >= l:
            if isPrime(nums[r]):
                break
            r -= 1
        return r - l