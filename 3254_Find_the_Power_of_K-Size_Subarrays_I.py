# class Solution:
#     def resultsArray(self, nums: List[int], k: int) -> List[int]:
# if k == 1:
# return nums
#         n = len(nums)
#         pref = [0] * (n + 1)
#         ascending = [1] * (n)
#         res = []
#         # pref[0] = nums[0]
#         # print(nums)
#         for i in range(1, n + 1):
#             pref[i] = pref[i - 1] + nums[i - 1]
#             if i < n:
#                 ascending[i] = ascending[i-1]+1 if nums[i]- nums[i-1]==1 else 1
#         # print(pref)
#         # print(ascending)
#         for i in range(k, n + 1):
#             sm = pref[i] - pref[i - k]
#             arifmetic = (nums[i-1] + nums[i-k])/2 * k
#             # print(sm, ascending[i-1], arifmetic)
#             if ascending[i-1] >=k and sm == arifmetic:
#                 res.append(nums[i-1])
#             else:
#                 res.append(-1)


#         return res
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums[:]
        n = len(nums)
        res = [-1] * (n - k + 1)
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[j - 1] + 1:
                j += 1
                if j - i >= k: res[j - k] = nums[j - 1]
            i = j
        #
        return res