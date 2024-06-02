
class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        @cache
        def f(l,r,s):
            if l > r:
                return 0
            al = 0
            bob = 0
            if s:
                al = max(f(l,r-1, 0)+nums[r] , f(l+1,r, 0)+nums[l])
            else:
                bob = max(f(l,r-1, 1) +nums[r], f(l+1,r, 1)+nums[l])
            return al > bob
        return  f(0,len(nums)-1,1)