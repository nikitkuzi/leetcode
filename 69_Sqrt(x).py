class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = 2 ** 16
        while l <= r:
            mid = (l + r) // 2
            if (mid - 1) ** 2 <= x < mid ** 2:
                return mid - 1
            if mid ** 2 > x:
                r = mid - 1
            else:
                l = mid + 1
