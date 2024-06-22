class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = Counter(s)
        b = Counter(t)
        for k, v in b.items():
            if k not in a:
                return k
            if v != a[k]:
                return k
