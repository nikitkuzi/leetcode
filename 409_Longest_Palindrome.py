class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        odd = 0
        for n in cnt.values():
            res += (n // 2)*2
            if n % 2:
                odd = 1
        if odd:
            res += 1
        return res