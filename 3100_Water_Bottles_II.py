class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0
        while numBottles+empty >= numExchange:
            if empty < numExchange:
                empty += numBottles
                ans+=numBottles
                numBottles = 0
            while empty >= numExchange:
                empty -= numExchange
                numBottles+=1
                numExchange+=1
        ans+= numBottles
        return ans