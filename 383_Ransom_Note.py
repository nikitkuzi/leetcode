class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True


test = Solution()

ransomNote = "abc"
magazine = "ba"

print(test.canConstruct(ransomNote, magazine))
