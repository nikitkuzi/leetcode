from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        index = 0
        for c in t:
            if index == n:
                break
            if c == s[index]:
                index += 1
        return n == index


test = Solution()
s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdca"
print(test.isSubsequence(s,t))

