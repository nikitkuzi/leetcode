class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def f(s):
            if len(s) == n:
                res.append(s)
                return
            if s and s[-1] == '0':
                f(s+'1')
            else:
                f(s+'0')
                f(s+'1')
        f('')
        return res