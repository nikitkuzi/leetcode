# class Solution:
#     def sumOfPowers(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)
#         ans = 0
#         dp = [[inf for i in range(n)] for _ in range(n)]
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 dp[i][j] = min(dp[i][j-1], nums[j]-nums[j-1])
#         for row in dp:
#             print(row)
#         for i in range(n-k+1):
#             print(i, i+k-1)
#             print(nums[i:i+k])
#             ans+= dp[i][i+k-1]

#         return ans
# class Solution:
#     def sumOfPowers(self, nums: List[int], k: int) -> int:
#         MOD = 10 ** 9 + 7
#         nums.sort()
#         ans = 0
#         @cache
#         def dp(idx, min_diff, last_choose, left_k):
#             if left_k == 0:
#                 if min_diff != inf:
#                     return min_diff
#                 else:
#                     return 0
#             if idx == len(nums):
#                 return 0
#             choose = dp(idx+1, min(min_diff, abs(last_choose-nums[idx])), nums[idx], left_k-1)
#             not_choose = dp(idx+1, min_diff, last_choose, left_k)
#             return (choose + not_choose) % MOD
#         return dp(0, inf, inf, k)
class Solution:
    def sumOfPowers(self, nums: List[int], kk: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()

        @cache
        def diff(i, k):
            ans = defaultdict(int)
            if k == 2:
                for j in range(i):
                    ans[abs(nums[i] - nums[j])] += 1
            else:
                for j in range(k - 2, i):
                    d = abs(nums[i] - nums[j])
                    dic = diff(j, k - 1)
                    for key in dic:
                        v = dic[key]
                        if d < key:
                            ans[d] += v
                        else:
                            ans[key] += v
            return ans

        ret = 0
        for i in range(kk - 1, n):
            dic = diff(i, kk)
            for key in dic:
                v = dic[key]
                ret += key * v
                ret %= MOD
        return ret