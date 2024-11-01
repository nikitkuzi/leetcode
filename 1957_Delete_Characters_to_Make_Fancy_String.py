class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = [''] * len(s)
        k = 0
        cnt = 1
        prev = None
        for c in s:
            if c == prev:
                cnt += 1
            else:
                cnt = 1
            prev = c
            if cnt < 3:
                ret[k] = c
                k += 1
        return ''.join(ret[:k])
