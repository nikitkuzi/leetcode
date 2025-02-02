class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        odd = [v for k,v in c.items() if v % 2 == 1]
        ev = [v for k,v in c.items() if v % 2 == 0]
        return max(odd) - min(ev)