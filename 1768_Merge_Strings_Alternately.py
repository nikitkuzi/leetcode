class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0
        j = 0
        while i < len(word1) and j<len(word2):
            ans.append(word1[i])
            ans.append(word2[i])
            i+=1
            j+=1
        if i != len(word1):
            ans.append(word1[i:])
        elif j != len(word2):
            ans.append(word2[j:])
        return "".join(ans)
