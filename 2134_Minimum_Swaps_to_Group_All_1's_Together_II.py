class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sm = sum(nums)
        l, r = 0, sm-1
        w = sum(nums[:r+1])
        # print(w)
        mn = sm-w
        for wind in range(r+1, len(nums)+sm+1):
            w += nums[wind%len(nums)] - nums[l%len(nums)]
            l+=1
            # print(w)
            mn = min(mn, sm-w)
        return mn
