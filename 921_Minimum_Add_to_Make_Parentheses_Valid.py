class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        cl = 0
        for c in s:
            if c == "(":
                op +=1
            else:
                cl+=1
        return abs(op-cl)