class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for j in range(k):
            mn = inf
            pos = -1
            for i, n in enumerate(nums):
                if mn > n:
                    mn = n
                    pos = i
            nums[pos] *= multiplier
        return nums
