class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3:
            return True
        if not s1 and s3 == s2:
            return True
        if not s2 and s3 == s1:
            return True

        @cache
        def f(ss1, ss2, ss3):
            if not ss3:
                # return ss1 != s1 and ss2 != s2
                return not ss1 and not ss2
            ans = False
            if ss1 and ss1[0] == ss3[0]:
                ans = f(ss1[1:], ss2, ss3[1:])
            if not ans and ss2 and ss2[0] == ss3[0]:
                ans = f(ss1, ss2[1:], ss3[1:])

            return ans

        return f(s1, s2, s3)




