class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                res+=1
        return res