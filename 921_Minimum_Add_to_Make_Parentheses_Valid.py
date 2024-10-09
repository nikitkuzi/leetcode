class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        cl = 0
        res = 0
        for c in s:
            if c == "(":
                op +=1
            else:
                op -= 1
            if op < 0:
                res +=1
                op = 0
        return abs(op)+res