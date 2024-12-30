class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        alph = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(len(words)):
            for j in range(n):
                alph[j][words[i][j]]+=1
        # dp[i][j] i - first i letters from words
        # j - first j letters from target
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j]
                if target[j-1] in alph[i-1]:
                    dp[i][j] += alph[i-1][target[j-1]]*dp[i-1][j-1]
        # for d in dp:
        #     print(d)
        return dp[-1][-1]%(10**9+7)
