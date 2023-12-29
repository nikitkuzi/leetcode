class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse=True)
        smallest_coin = coins[-1]

        # smallest_coin = min(coins)

        @cache
        def get_coins(amount):
            if amount == 0:
                return 0
            if amount < 0 or amount < smallest_coin:
                return float(inf)

            res = float(inf)
            for c in coins:
                if amount / c > res:
                    break
                res = min(res, 1 + get_coins(amount - c))

            return res

        res = get_coins(amount)
        return res if res != float(inf) else -1