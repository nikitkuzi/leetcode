class Solution:
    def scoreOfString(self, s: str) -> int:
        d = {letter:ord(letter) for letter in string.ascii_lowercase}
        return sum(abs(d[s[i]]-d[s[i+1]]) for i in range(len(s)-1))