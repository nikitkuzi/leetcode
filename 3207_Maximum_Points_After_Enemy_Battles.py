# class Solution:
#     def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
#         mn = min(enemyEnergies)
#         sm = sum(enemyEnergies)
#         if mn > currentEnergy:
#             return 0
#         currentEnergy -= mn
#         res = 1
#         currentEnergy += (sm-mn)
#         res += (currentEnergy // mn)
#         return res
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        mn = inf
        sm = 0
        for n in enemyEnergies:
            if mn > n:
                mn = n
            sm += n
        if mn > currentEnergy:
            return 0
        currentEnergy -= mn
        res = 1
        currentEnergy += (sm-mn)
        res += (currentEnergy // mn)
        return res