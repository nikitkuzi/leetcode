class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        ones = sum(possible)
        zeros = len(possible)-ones
        alice = 0
        bob = ones-zeros
        for i, num in enumerate(possible):
            if num:
                alice+=1
                bob-=1
            else:
                alice-=1
                bob+=1
            if alice>bob:
                return -1 if i == len(possible)-1 else i+1
        return -1
