# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         b = {5:0, 10:0, 20:0}
#         for n in bills:
#             if n == 5:
#                 b[5]+=1
#                 continue
#             b[n]+=1
#             change = n - 5
#             if change >= 10 and b[10] > 0:
#                 b[10] -= 1
#                 change -= 10
#             if change >= 5:
#                 if change // 5 > b[5]:
#                     return False
#                 else:
#                     b[5]-=change//5
#         return True

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5: five += 1
            elif i == 10: five, ten = five - 1, ten + 1
            elif ten > 0: five, ten = five - 1, ten - 1
            else: five -= 3
            if five < 0: return False
        return True