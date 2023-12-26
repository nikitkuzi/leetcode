from math import log2


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Initialize a variable 'shift' to 0.
        shift = 0
        print(bin(left),bin(right))
        # While the left and right limits are not equal,
        while left < right:
            # Right shift the left limit by 1 bit.
            left >>= 1
            # left //=2
            # Right shift the right limit by 1 bit.
            right >>= 1
            # right//=2
            # Increment the 'shift' variable by 1.
            shift += 1
            print(bin(left),bin(right))
        # Left shift the left limit by 'shift' bits and return the result.
        return right << shift
test = Solution()
print(test.rangeBitwiseAnd(1,505))