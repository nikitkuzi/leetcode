class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [0] * n
        dp[0] = values[0]
        for i in range(1, n):

