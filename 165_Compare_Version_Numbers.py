class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def conv(s):
            while s[-2:] == '.0':
                s = s[:-2]
            return s

        s11 = conv(version1).split(".")
        s22 = conv(version2).split(".")
        res = 0
        if len(s11) > len(s22):
            for i in range((len(s11) - len(s22))):
                s22.append("0")
        elif len(s11) < len(s22):
            for i in range((len(s22) - len(s11))):
                s11.append("0")
        # print(s11)
        # print(s22)
        for s1, s2 in zip(s11, s22):
            if int(s1) < int(s2):
                return -1
            elif int(s1) > int(s2):
                return 1

        return res

