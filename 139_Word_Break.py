class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        # mxlen = max(map(len,wordDict))
        for i in range(len(s) + 1):
            for word in wordDict:

                if len(word) > i:
                    continue
                # print(dp,word,s[i-len(word):i])
                if (i - len(word) == 0 and s[i - len(word):i] == word) or (
                        dp[i - len(word) - 1] and s[i - len(word):i] == word):
                    dp[i - 1] = True
                    break
                # elif dp[i-len(word)] and s[i-len(word):i] == word:
                # dp[i-1] = True
                # break
        # print(dp)
        return dp[-1]