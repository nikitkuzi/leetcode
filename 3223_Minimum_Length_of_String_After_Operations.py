class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        res = 0
        for char, n in c.items():
            res+=1
            if not n%2:
                res+=1
        return res