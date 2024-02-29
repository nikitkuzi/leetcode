# class Solution:
#     def minFlips(self, a: int, b: int, c: int) -> int:
#         n = len(bin(c))-2
#         ans = 0
#         while n:
#             print(c&1, a&1, b&1, (a&1 | b & 1 ) ,not(a&1 | b & 1 ), int(a&1)+int(b&1))
#             if c & 1 == 1:
#                 ans += not(a&1 | b & 1 )
#             else:
#                 ans += int(a&1) + int(b&1)
#             a >>=1
#             b >>=1
#             c>>=1
#             n-=1
#         ans+= a.bit_count()
#         ans+=b.bit_count()
#         return ans
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        m = (a|b)^c
        x = a&m
        y = b&m
        z = (~(a|b))&m
        # print(bin(a),bin(b),bin(c))
        # print(bin(m), bin(x), bin(y), bin(z))
        return sum(v.bit_count() for v in (x,y,z))
        # return x.bit_count()+y.bit_count()+z.bit_count()