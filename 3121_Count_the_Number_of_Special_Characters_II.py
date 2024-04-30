# class Solution:
#     def numberOfSpecialChars(self, word: str) -> int:
#         ans = 0
#         bad = ""
#         lower = defaultdict(int)
#         upper = {}
#         for i, l in enumerate(word):
#             if l.islower():
#                 lower[l] = i
#             else:
#                 if l not in upper:
#                     upper[l] = i
#         for k,v in lower.items():
#             if k.upper() in upper and upper[k.upper()] > v:
#                 ans += 1
#         return ans
class Solution:
    def numberOfSpecialChars(self, word: str, ans=0) -> int:

        for ch, CH in zip(ascii_lowercase, ascii_uppercase):

            if ch not in word or CH not in word: continue

            ans += word.rfind(ch) < word.find(CH)

        return ans