class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1,str2  = str2, str1
        ans = ""
        for i in range(len(str1)):
            # print(str1[:i+1], len(str1)//(i+1),len(str2)//(i+1))
            # print(str1[:i+1]*5)
            if (str1 == str1[:i+1]*(len(str1)//(i+1))) and (str2 == str1[:i+1]*(len(str2)//(i+1))):
                ans = str1[:i+1]
        return ans

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]