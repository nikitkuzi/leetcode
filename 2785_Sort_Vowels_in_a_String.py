# class Solution:
#     def sortVowels(self, s: str) -> str:
#         n = len(s)
#         res = [""]*n
#         vov = []
#         pos = []
#         for i in range(n):
#             if s[i].lower() not in "aeiou":
#                 res[i] = s[i]
#             else:
#                 pos.append(i)
#                 vov.append(s[i])
#         vov.sort(key=lambda x:ord(x))
#         for p, v in zip(pos, vov):
#             res[p] = v
#         return "".join(res)
class Solution:
    def sortVowels(self, s: str) -> str:
        freq=Counter(s)
        vowel='AEIOUaeiou'
        count, v, j=0, freq['A'], 0
        s=list(s)
        for i, c in enumerate(s):
            if c not in vowel: continue
            while count>=v:
                j+=1
                v+=freq[vowel[j]]
            s[i]=vowel[j]
            count+=1
        return "".join(s)