class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        last = 0
        for num in nums:
            l = 0
            r = last - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            last = max(last, l + 1)
            tails[l] = num
            # print(tails)
        return last
