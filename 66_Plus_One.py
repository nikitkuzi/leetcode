class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        while (n >= 0 and digits[n] == 9):
            digits[n] = 0
            n -= 1
        if n < 0:
            digits.insert(0, 1)
        if n >= 0 and digits[n] != 9:
            digits[n] += 1

        return digits