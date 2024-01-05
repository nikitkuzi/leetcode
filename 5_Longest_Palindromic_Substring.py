class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]
        mx = 0
        st = s[0]
        for i in range(len(s)):
            dp[i][i] = 1
            for j in range(i):
                if s[j] == s[i] and ((i-j < 3) or dp[i-1][j+1]):
                    dp[i][j] = 1
                    if i-j > mx:
                        mx= i-j
                        st = s[j:i+1]
        # print(dp)
        return st