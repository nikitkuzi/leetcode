class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        summ = 0
        ans = 0
        index = 0
        for i in range(len(gas)-1, -1, -1):
            summ += (gas[i] - cost[i])
            if ans < summ:
                ans = summ
                index = i
        return index
test = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(test.canCompleteCircuit(gas,cost))
print('=====')
gas = [12,0,0,6,0]
cost = [5,5,1,5,2]
print(test.canCompleteCircuit(gas,cost))
print('=====')
gas = [0,12,0,0,6,2]
cost = [2,5,5,1,5,2]
print(test.canCompleteCircuit(gas,cost))