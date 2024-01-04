class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        mx = 0
        st = ""
        for i in range(len(s)):
            dp[i][i] = 1
            for j in range(i):
                if s[j] == s[i] and ((i-j < 3) or dp[j+1][i-1]):
                    dp[j][i] = 1
                    if i-j > mx:
                        mx= i-j
                        st = s[j:i+1]
        return st