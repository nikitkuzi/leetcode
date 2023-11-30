class Solution:
    def reverseWords(self, s: str) -> str:
        s.replace('  ', ' ')
        s.strip()
        return " ".join(s.split()[::-1])
        # return " ".join(s.split()[::-1])


test = Solution()
s = "the sky is blue"
print(test.reverseWords(s))