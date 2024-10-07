class Solution:
    def minLength(self, s: str) -> int:
        res = []
        for c in s:
            if not res:
                res.append(c)
                continue
            if c == 'B' and res[-1] == 'A':
                res.pop()
                continue
            if c == 'D' and res[-1] == 'C':
                res.pop()
                continue
            res.append(c)
        return len(res)


