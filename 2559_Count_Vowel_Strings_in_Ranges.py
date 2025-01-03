class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pref = [0]+[0] * len(words)
        for i in range(len(words)):
            pref[i+1] += pref[i] + (words[i][0] in "aeiou" and words[i][-1] in "aeiou")
        res = [0]*len(queries)
        # print(pref)
        for i, q in enumerate(queries):
            res[i] = pref[q[1]+1] - pref[q[0]]
        return res