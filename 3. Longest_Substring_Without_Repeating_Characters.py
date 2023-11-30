from collections import Counter, defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length
test = Solution()
# s = "abcabcbb"
# s = "abcadefgh"
# s = "abcaadefgh"
# s = "ab"
s = "ohvhjdml"
# s = "aabaab!bb"

print(test.lengthOfLongestSubstring(s))
