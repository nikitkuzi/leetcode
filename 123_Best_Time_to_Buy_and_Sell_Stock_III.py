class Solution:
  def maxProfit(self, prices: List[int]) -> int:

    dp = [[float(inf),0] for _ in range(3)]

    # iterate over prices to update buy and sell values
    for price in prices:
        for i in range(1,3):
            dp[i][0] = min(dp[i][0], price - dp[i-1][1])
            dp[i][1] = max(dp[i][1],price-dp[i][0])
    return dp[2][1]
