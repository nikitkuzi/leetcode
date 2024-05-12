class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        subs = {}
        for i in range(len(s)-1):
            subs[s[i:i+2]]=1
            if (s[i+1]+s[i]) in subs:
                return True
        return False