class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0]*(high+1)
        res = 0
        MOD = (10**9+7)
        dp[zero] += 1
        dp[one] += 1
        # print(dp)
        for i in range(min(zero, one), high+1):
            dp[i] += (dp[i-zero]+dp[i-one])%MOD
            if low <= i <= high:
                res += dp[i]
        # print(dp)
        return res % MOD