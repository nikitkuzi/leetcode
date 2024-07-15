class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split()
        for i, word in enumerate(t):
            t[i] = t[i][::-1]
        return " ".join(t)
