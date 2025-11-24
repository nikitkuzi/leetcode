class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        res = []
        for n in nums:
            if n == 0:
                curr*=2
            else:
                curr = curr*2 + 1
            if curr % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res