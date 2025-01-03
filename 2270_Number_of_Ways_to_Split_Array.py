class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = [0]*len(nums)
        suf = [0]*len(nums)+[0]
        for i in range(len(nums)):
            pref[i] = pref[i-1] + nums[i]
            suf[-i-2] = suf[-i-1]+nums[-i-1]
        res = 0
        # print(pref)
        # print(suf)
        for i in range(len(nums)-1):
            # print(pref[i], suf[i+1])
            if pref[i] >= suf[i+1]:
                res+=1
        return res