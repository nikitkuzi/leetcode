class Solution:
    def isPalindrome(self, s: str) -> bool:
        extracted_string = ''.join(filter(str.isalnum, s)).lower()
        return extracted_string == extracted_string[::-1]
test = Solution()
# s = "A man, a plan, a canal: Panama"
s = "A man, a plan, a analh: Panama"
# s = "A man, a plan, a anal: Panama"
s = " "
print(test.isPalindrome(s))

