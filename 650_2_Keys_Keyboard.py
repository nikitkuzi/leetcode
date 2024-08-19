class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        res = 1
        curr_copy = 1
        curr_len = 1
        while curr_len < n:
            if n % curr_len == 0 and curr_copy != curr_len:
                curr_copy = curr_len
            else:
                curr_len += curr_copy
            res+=1
        return res



# class Solution:
#     def get_primes(self, n):
#         res = [True] * (n+1)
#         p = 2
#         while p * p <= n:
#             if res[p] == True:
#                 for i in range(p*2, n+1, p):
#                     res[i] = False
#             p += 1
#         return res


#     def minSteps(self, n: int) -> int:
#         primes = self.get_primes(n)
#         if n == 1:
#             return 0
#         if primes[n]:
#             return n
#         res = [i if primes[i] == True else inf for i in range(n+1)]
#         res[1] = 0
#         for i in range(1, n+1):
#             if i % 2 == 0:
#                 res[i] = res[i//2] + 2
#             else:
#                 for divisor in range(3, i//2+1):
#                     if i % divisor == 0:
#                         res[i] = min(res[i//divisor]+divisor, res[divisor]+(i//divisor))
#         return res[n]