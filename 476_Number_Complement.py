class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        temp = num
        while temp > 0:
            count += 1
            temp >>= 1
        return num ^ (2**count - 1)