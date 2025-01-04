# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         res = 0
#         d = dict()
#         seen = [0]*128
#         se = set()
#         shift = ord('a')
#         for i, c in enumerate(s):
#             # print(i, c)
#             char_pos = ord(c)
#             for visited in se:
#                 if c != visited:
#                     d[visited].add(c)
#             if c not in d:
#                 # print('here1')
#                 d[c] = set()
#                 se.add(c)
#             elif seen[char_pos] == 0:
#                 # print('here2')
#                 seen[char_pos] = len(d[c])
#                 res += seen[char_pos]
#                 if len(d[c]) == 0:
#                     d[c].add(c)
#             elif seen[char_pos]:
#                 # print('here3')
#                 res -= seen[char_pos]
#                 d[c].add(c)
#                 seen[char_pos] = len(d[c])
#                 res += seen[char_pos]

#         # for i in range(26):
#             # print(chr(i+ord('a')), seen[i], end = ' ')
#         # print()
#         # print(d)
#         # for i in range(26):
#             # if seen[i]:
#                 # res+=len(d[chr(i+ord('a'))])
#         return res
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for ch in range(26):
            c = chr(ord('a') + ch)
            leftIdx, rightIdx = s.find(c), s.rfind(c)
            if leftIdx != rightIdx:
                res += len(set(s[leftIdx+1:rightIdx]))
        return res