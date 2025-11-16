class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        one = 0
        MOD = 10 ** 9 + 7
        i = 0
        while i < len(s):
            if s[i] == '0':
                i += 1
                one = 0
                continue
            while i < len(s) and s[i] == '1':
                one += 1
                i += 1

            res = (res + one * (one + 1) // 2) % MOD

        return res
