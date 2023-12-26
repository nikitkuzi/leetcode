class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        potential_profit = 0
        total_profit = 0
        for i, price in enumerate(prices[1:]):
            # print(f"buy:{buy}, sell:{sell}")
            # if price > buy and price < sell:
            if price < sell:
                total_profit -= potential_profit
                potential_profit = 0
                total_profit += sell - buy
                buy = price
                sell = price
                # print(f"total_profit:{total_profit}")
            elif price > buy:
                total_profit -= potential_profit
                sell = price
                potential_profit = sell - buy
                total_profit += potential_profit

        return total_profit
test = Solution()
nums = [2,1,3,3,4,5]
test.maxProfit(nums)