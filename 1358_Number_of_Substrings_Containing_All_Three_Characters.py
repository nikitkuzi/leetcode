# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         last_pos = [-1]*3
#         total = 0
#
#         for pos in range(len(s)):
#             last_pos[ord(s[pos])-ord('a')] = pos
#             total += 1+min(last_pos)
#         return total

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = [[-inf, -inf, -inf] for _ in range(len(s))]
        pos[-1][ord(s[-1])-ord('a')] = len(s)-1
        res = 0
        for i in range(len(s)-2, -1, -1):
            pos[i][ord(s[i])-ord('a')] = i
            for j in range(3):
                if pos[i][j] == -inf:
                    pos[i][j] = pos[i+1][j]
        # print(pos)
        for i in range(len(s)):
            if any(x==-inf for x in pos[i]):
                break
            res+=len(s)-max(pos[i])
        return res