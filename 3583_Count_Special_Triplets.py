class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freqPrev, freqNext = Counter(), Counter(nums)
        count = 0
        MOD = 10**9+7
        for num in nums:
            freqNext[num] -= 1
            count = (count + freqPrev[num*2] * freqNext[num*2])%MOD
            freqPrev[num] += 1
        return count