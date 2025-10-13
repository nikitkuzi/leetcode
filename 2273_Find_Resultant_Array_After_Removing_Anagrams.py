class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            if not res:
                res.append(w)
                continue
            if sorted(w) == sorted(res[-1]):
                continue
            else:
                res.append(w)
        return res
