class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        cnt = 0
        pre = None
        for c in word:
            if pre is None:
                cnt = 1
                pre = c
            elif c != pre:
                res.append(str(cnt))
                res.append(pre)
                cnt = 1
                pre = c
            else:
                if cnt < 9:
                    cnt += 1
                else:
                    res.append('9')
                    res.append(pre)
                    cnt = 1
        res.append(str(cnt))
        res.append(pre)
        return "".join(res)