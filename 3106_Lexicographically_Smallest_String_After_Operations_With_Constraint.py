class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = ""
        for i, char in enumerate(s):
            last = i
            number = ord(char)-97
            if k > 26 or number + k >= 26 or number-k <= 0:
                ans+="a"
                k-= min(number, 26-number)
            else:
                ans+=str(chr(number-k+97))
                k=0
            if k == 0:
                break
        if last!= len(s)-1:
            ans+=s[last+1:]
        return ans