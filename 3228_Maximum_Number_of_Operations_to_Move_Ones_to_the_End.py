class Solution:
    def maxOperations(self, s: str, res=0, cnt=0) -> int:

        arr = list(map(len, s.split('0')))

        for num in arr:

            if num == 0: continue
            cnt += num
            res += cnt

        return res if arr[-1] == 0 else res - cnt
# class Solution:
#     def maxOperations(self, s: str) -> int:
#         if len(s)==1:
#             return 0
#         i = -1
#         while i > -len(s) and s[i]=='1':
#             i-=1
#         if i == -len(s):
#             return 0
#         if i!=-1:
#             s = s[:i+1]
#         res = 0
#         ones = 0
#         i = 0
#         # print(s)
#         while i < len(s):
#             if s[i] == '1':
#                 while s[i] == '1':
#                     ones += 1
#                     i+=1
#                 res += ones
#                 i-=1
#             i += 1
#         return res
