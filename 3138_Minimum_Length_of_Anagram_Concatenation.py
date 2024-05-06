class Solution:
    def minAnagramLength(self, s: str) -> int:
        mn = inf
        steps = []
        for i in range(1, int(sqrt(len(s)) + 1)):
            if len(s) % i == 0:
                steps.append(i)
                steps.append(len(s) // i)
        steps.sort()
        if len(set(s)) == 1:
            return 1
        for i in steps:
            anag = Counter(s[:i])
            f = True
            for j in range(i, len(s), i):
                if anag != Counter(s[j:j + i]):
                    f = False
                    break
            if f:
                return i
        # return mn
