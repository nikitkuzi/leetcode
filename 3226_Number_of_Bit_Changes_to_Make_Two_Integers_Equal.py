# class Solution:
#     def minChanges(self, n: int, k: int) -> int:
#         res = 0
#         while k:
#             if k & 1 != n & 1:
#                 if k&1==1:
#                     return -1
#                 else:
#                     res+=1
#             k>>=1
#             n>>=1
#             # print(k,n)
#         while n:
#             res+=int(n&1)
#             n>>=1
#         return res 

def cardinality(bitset: int):
    ones_count = 0
    while bitset:
        ones_count += (bitset & 1)
        bitset >>= 1
    return ones_count


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        a = (n ^ k)
        b = a & n
        if a == b:
            return cardinality(a)
        else:
            return -1