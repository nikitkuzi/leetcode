class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        if c1 == c2:
            return True
        for i in range(len(s1), len(s2)):

            c2[s2[i - len(s1)]] -= 1

            c2[s2[i]] += 1

            if c1 == c2:
                return True
        return False