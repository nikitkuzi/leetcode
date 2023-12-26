class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        max_profit = 0
        for i, price in enumerate(prices[1:]):
            current_profit = price - buy
            max_profit = max(max_profit, current_profit)
            if price < buy:
                buy = price

        print(max_profit)
test = Solution()
nums = [7,6,4,3,1]
test.maxProfit(nums)