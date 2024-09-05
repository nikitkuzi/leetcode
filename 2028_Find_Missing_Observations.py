# class Solution:
#     def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
#         sm = sum(rolls)
#         m = len(rolls)
#         needed = mean*(n+m) - sm
#         # print(sm, needed)
#         if n > needed or 6*n < needed:
#             return []
#         res = []
#         for dice in range(6, 0, -1):
#             if dice == 1:
#                 res.extend([1]*n)
#                 break
#             x = (n - needed) // (1-dice)
#             res.extend([dice]*x)
#             needed -= x*dice
#             n -= x
#         return res
# class Solution:
#     def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
#         m = len(rolls)
#         totalSum = mean * (m + n)
#         rollsSum = sum(rolls)

#         missingSum = totalSum - rollsSum

#         if missingSum < n or missingSum > 6 * n:
#             return []

#         quotient, remainder = divmod(missingSum, n)
#         return [quotient + (1 if i < remainder else 0) for i in range(n)]
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        curSum = sum(rolls)
        obv = n + len(rolls)
        missSum = mean * obv - curSum
        if missSum > 6 * n or missSum < 0 or missSum < n:
            return []
        x = missSum // n
        res = [x] * n
        remain = missSum - x * n
        if remain > 0:
            more = 6 - x
            add = remain // more
            res = res[add:] + [6] * add
            final = remain % more
            res[0] += final
        return res
