class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        M = 10**9 + 7
        dp = [[[0] * 2 for _ in range(zero + 1)] for _ in range(one + 1)]
        dp[0][0][0] = dp[0][0][1] = 1
        for o in range(one + 1):
            for z in range(zero + 1):
                for lim in range(1, limit + 1):
                    if o - lim >= 0:
                        dp[o][z][1] = (dp[o][z][1] + dp[o - lim][z][0]) % M
                    if z - lim >= 0:
                        dp[o][z][0] = (dp[o][z][0] + dp[o][z - lim][1]) % M
        return (dp[one][zero][0] + dp[one][zero][1]) % M