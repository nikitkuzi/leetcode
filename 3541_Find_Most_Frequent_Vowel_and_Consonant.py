class Solution:
    def maxFreqSum(self, s: str) -> int:
        con = defaultdict(int)
        vow = defaultdict(int)
        c = 0
        v = 0
        for i in s:
            if i in "aeiou":
                vow[i]+=1
                v = max(v, vow[i])
            else:
                con[i]+=1
                c = max(c, con[i])
        return v+c