class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3:
            return True
        if not s1 and s3 == s2:
            return True
        if not s2 and s3 == s1:
            return True

        @cache
        def f(ss1, ss2, ss3):
            if not ss3:
                # return ss1 != s1 and ss2 != s2
                return not ss1 and not ss2
            ans = False
            if ss1 and ss1[0] == ss3[0]:
                ans = f(ss1[1:], ss2, ss3[1:])
            if not ans and ss2 and ss2[0] == ss3[0]:
                ans = f(ss1, ss2[1:], ss3[1:])

            return ans

        return f(s1, s2, s3)


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m, n, l = len(s1), len(s2), len(s3)
#         if m + n != l:
#             return False
#
#         dp = [[False] * (n + 1) for _ in range(m + 1)]
#         dp[0][0] = True
#
#         for i in range(1, m + 1):
#             dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
#
#         for j in range(1, n + 1):
#             dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
#
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
#                             dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
#
#         return dp[m][n]

