class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = Counter(s)
        d2 = Counter(t)
        return d == d2


test = Solution()

s = "badc"
t = "baba"
print(test.isIsomorphic(s, t))
