class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for word in words:
            f = True
            for c in word:
                if c not in allowed:
                    f = False
                    break
            if f:
                res+=1
        return res