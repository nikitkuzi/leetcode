# class Solution:
#     def getSmallestString(self, s: str) -> str:
#         for i in range(len(s)-1):
#             if int(s[i])%2 == int(s[i+1])%2:
#                 if int(s[i]) > int(s[i+1]):
#                     return s[:i]+s[i+1]+s[i]+s[i+2:]
#         return s
class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n - 1):
            if int(s[i]) > int(s[i + 1]):
                if (int(s[i]) % 2 == int(s[i + 1]) % 2):
                    s[i], s[i + 1] = s[i + 1], s[i]
                    break
        return ''.join(s)