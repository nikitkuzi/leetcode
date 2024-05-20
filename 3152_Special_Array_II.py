class Solution:
    def isArraySpecial(self, nums: List[int], quer: List[List[int]]) -> List[bool]:
        n = len(nums)
        cnts = [0] * n
        for i in range(1, n):
            if nums[i] % 2 == nums[i-1] % 2: cnts[i] = cnts[i-1] + 1
            else: cnts[i] = cnts[i-1]
        ans = []
        for x, y in quer:
            ans.append(cnts[x] == cnts[y])
        return ans