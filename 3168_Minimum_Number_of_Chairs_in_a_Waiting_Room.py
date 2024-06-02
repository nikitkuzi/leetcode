class Solution:
    def minimumChairs(self, s: str) -> int:
        e = 0
        mx = 0
        for c in s:
            if c=='E':
                e+=1
                mx = max(e,mx)
            else:
                e-=1
        return mx