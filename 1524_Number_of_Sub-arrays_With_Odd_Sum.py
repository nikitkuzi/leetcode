class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cumSum = odd = even = 0
        for num in arr:
            cumSum += num
            if cumSum % 2:
                odd += 1
            else:
                even += 1
        return odd * (even + 1) % (pow(10, 9) + 7)