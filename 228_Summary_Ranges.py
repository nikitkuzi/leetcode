class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        if len(nums) == 0:
            return ans
        l, r = nums[0], nums[0]
        for i, num in enumerate(nums[1:], start=1):
            if num == r + 1:
                r = num
            else:
                if l == r:
                    ans.append(str(l))
                else:
                    ans.append(f"{str(l)}->{str(r)}")
                l = num
                r = num
        if l == r:
            ans.append(str(l))
        else:
            ans.append(f"{str(l)}->{str(r)}")
        return ans


test = Solution()
# nums = [0,1,2,4,5,7]
# nums = [0, 2, 3, 4, 6, 8, 9]
nums = [1]
print(test.summaryRanges(nums))
