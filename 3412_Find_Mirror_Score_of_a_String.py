class Solution:
    def calculateScore(self, s: str) -> int:
        d = defaultdict(list)
        #i 25 - i
        res = 0
        a = ord('a')
        z = ord('z')
        for i, c in enumerate(s):
            # d[c].append(i)
            mir = chr(a+z-ord(c))
            if mir in d and d[mir]:
                res += i-d[mir].pop()
            else:
                d[c].append(i)
        # for i, c in enumerate(string.ascii_lowercase):
        #     print(c, chr(a+z-ord(c)))
        return res