# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
#         for i in range(1,len(text1)+1):
#             for j in range(1, len(text2)+1):
#                 if text1[i-1] == text2[j-1]:
#                     dp[i][j] = dp[i-1][j-1]+1
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         return dp[-1][-1]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(text1):
            pos[c].append(i)

        lcs = [inf] * len(text2)

        for c in text2:
            for i in reversed(pos[c]):
                lcs[bisect_left(lcs, i)] = i

        return bisect_left(lcs, inf)