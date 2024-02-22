# class Solution:
#     def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
#         potions.sort()
#         ans = []
#         for spell in spells:
#             l = 0
#             r = len(potions)-1
#             while l<=r:
#                 mid = (l+r)//2
#                 # print(potions[mid], potions[mid]*spell, l, r)
#                 if potions[mid]*spell < success:
#                     l = mid+1
#                 else:
#                     r = mid-1

#             ans.append(len(potions)-l)
#         return ans
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        a = []
        potions.sort()
        m = len(potions)
        maxpotion = potions[m - 1]

        for i in spells:
            minpotion = (success + i - 1) // i
            if minpotion > maxpotion:
                a.append(0)
                continue
            index = bisect.bisect_left(potions, minpotion)
            a.append(m - index)
        return a