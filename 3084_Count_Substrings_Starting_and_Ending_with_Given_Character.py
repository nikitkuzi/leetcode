class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        ans = s.count(c)
        return  ans*(ans+1) // 2
