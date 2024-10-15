class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        zeros = 0
        ans = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                ans+= ones
        return ans