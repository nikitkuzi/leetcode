class Solution:
    def countSubstrings(self, s: str) -> int:
        # def ex(center):
        #     if center%2:
        #         l = center//2
        #     else:
        #         l = center//2-1
        #     r = center//2+1
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         nonlocal ans
        #         ans+=1
        #         l-=1
        #         r+=1
        # ans = len(s)
        # for c in range(2*len(s)):
        #     ex(c)
        # return ans
        dp = [[0 for _ in range(len(s))] for i in range(len(s))]
        ans = len(s)
        for i in range(len(s)):
            for j in range(i):
                dp[i][i]=1
                if s[i]==s[j] and (i-j<3 or dp[i-1][j+1]):
                    dp[i][j]=1
                    ans+=1
        return ans