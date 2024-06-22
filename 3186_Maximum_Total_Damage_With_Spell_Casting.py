class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        uniq = Counter(power)
        spells = [0, 0, 0] + sorted(list(uniq.keys()))
        n = len(spells)
        dp = [0]*n
        for i in range(3, n):
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + uniq[spells[i]]*spells[i]
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + uniq[spells[i]]*spells[i])
            else:
                dp[i] = max(dp[i-1], dp[i-3] + uniq[spells[i]]*spells[i])
        return dp[-1]