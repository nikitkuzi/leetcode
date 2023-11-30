class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        seen = set()
        if len(pattern) != len(s.split()):
            return False
        for c, word in zip(pattern, s.split()):
            if c not in d:
                if word in seen:
                    return False
                d[c] = word
                seen.add(word)
            elif d[c] != word:
                return False
        return True

test = Solution()

pattern = "abba"
s = "dog dog dog dog"
print(test.wordPattern(pattern, s))
