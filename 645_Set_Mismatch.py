class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        xorAll = 0
        xorArray = 0

        for i in range(1, n + 1):
            xorAll ^= i

        for num in nums:
            xorArray ^= num

        xorResult = xorArray ^ xorAll

        rightmostSetBit = xorResult & -xorResult

        xorSet = 0
        xorNotSet = 0

        for i in range(1, n + 1):
            if (i & rightmostSetBit) != 0:
                xorSet ^= i
            else:
                xorNotSet ^= i

        for num in nums:
            if (num & rightmostSetBit) != 0:
                xorSet ^= num
            else:
                xorNotSet ^= num

        for num in nums:
            if num == xorSet:
                return [xorSet, xorNotSet]

        return [xorNotSet, xorSet]