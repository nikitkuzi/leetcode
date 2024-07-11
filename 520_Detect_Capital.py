# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         if word.swapcase() == word.upper() or word.swapcase() == word.lower() or word == word.title():
#             return True
#         return False
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False