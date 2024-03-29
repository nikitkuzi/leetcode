class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        sbstr = set()
        for l in s:
            if l not in sbstr:
                sbstr.add(l)
            else:
                ans+=1
                sbstr = set(l)

        return ans