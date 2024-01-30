class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            if c is '*':
                ans.pop()
            else:
                ans.append(c)
        return "".join(ans)