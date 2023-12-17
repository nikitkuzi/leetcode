class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        mx = float("-inf")
        mn = float("inf")
        cx1 = 0
        cx2 = 0
        s = sum(nums)
        for n in nums:
            cx1 = max(n,n+cx1)
            cx2 = min(n,n+cx2)
            mx = max(mx,cx1)
            mn = min(mn,cx2)
        # print(cx1,cx2,mx,mn,max(mx,sum(nums)-mn))
        return mx if s == mn and 0 not in nums else max(mx,s-mn)
        # i = 0
        # n = len(nums)
        # lim = n
        # while i<lim and i < n*2:
        #     if nums[i%n]>(cx+nums[i%n]):
        #         lim = n+i
        #         cx = nums[i%n]
        #     else:
        #         cx+=nums[i%n]
        #     mx = max(mx,cx)
        #     i+=1
        # return mx