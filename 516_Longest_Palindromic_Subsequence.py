# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         t = s[::-1]
#         if s == t:
#             return len(s)
#         dp = [[0 for _ in range(len(t) + 1)] for i in range(len(s) + 1)]
#         ans = 0
#         for i in range(1, len(s) + 1):
#             dp[i][1] = (s[i - 1] == t[0]) ^ 1
#         for j in range(1, len(t) + 1):
#             dp[1][j] = (s[0] == t[j - 1]) ^ 1
#         for i in range(1, len(s) + 1):
#             for j in range(1, len(t) + 1):
#                 if s[i - 1] == t[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1] + 1

#                 else:
#                     dp[i][j] = max(dp[i-1][j-1], dp[i-1][j],dp[i][j-1])

#         return dp[-1][-1]
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        @cache
        def helper(start,end):
            if start>end:
                return 0
            if start==end:
                return 1
            # if start==end:
                # print(start,end,s[start],s[end])
            if s[start]==s[end]:
                return  2 + helper(start+1,end-1)
            else:
                return max(
                    helper(start+1,end),
                    helper(start,end-1)
                )
        return helper(0,len(s)-1)