class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        br = set(brokenLetters)
        res = 0
        for word in text.split():
            good = True
            for ch in word:
                if ch in br:
                    good = False
                    break
            if good:
                res+=1
        return res