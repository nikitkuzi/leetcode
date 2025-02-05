class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        for a,b in zip(s1, s2):
            if a!= b:
                c+=1
                if c > 2:
                    return False
        if (c == 0 or c == 2) and Counter(s1) == Counter(s2):
            return True
        return False