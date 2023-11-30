from collections import defaultdict
class Solution:
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for string in strings:
            hashed_string = "".join(sorted(string))
            anagrams[hashed_string].append(string)
        return anagrams.values()


test = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
test.groupAnagrams(strs)
