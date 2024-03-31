# class Solution:
#     def longestNiceSubstring(self, s: str) -> str:
#         mx = ""
#         l = 0
#         r = 1
#         while l <= len(s)-len(mx)-1 and r < len(s):
#             counter = defaultdict(int)
#             r = l+1

#             counter[s[l]] = 1
#             while r<len(s):
#                 counter[s[r]] += 1
#                 # print(s[l:r+1], check(counter), r-l, len(mx))
#                 if check(counter) and 1+r-l > len(mx):
#                     mx = s[l:r+1]
#                 r+=1
#             l+=1
#             r = 0
#             # print()
#         return mx
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        if n < 2: return ""
        rt = ""
        ss = set(s)
        for ii in range(n):
            if s[ii].swapcase() not in ss:
                s1 = self.longestNiceSubstring(s[0:ii])
                s2 = self.longestNiceSubstring(s[ii + 1:])
                return max(s1, s2, key=len)
        return s