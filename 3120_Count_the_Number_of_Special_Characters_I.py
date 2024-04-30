class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d = set(word)
        ans = 0
        for w in d:
            if w.lower() == w and w.upper() in d:
                ans+=1
        return ans