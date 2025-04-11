class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        l, h = str(low-1), str(high)
        return self.dp(h, len(h), 0, True, len(h)) - self.dp(l, len(l), 0, True, len(l))

    @cache
    def dp(self, num, left, s, tight, first):
        if left == 0:
            return s == 0 and 1 - first % 2
        digit = int(num[-left])
        ub = 9 if not tight else digit
        lb = 0 if first != left else 1
        ans = 0
        sgn = 1-2*(left*2 <= first)
        for i in range(lb, ub+1):
            ans += self.dp(num, left-1, s + sgn * i, tight and digit == i, first)
        if first == left:
            ans += self.dp(num, left-1, s, False, first-1)
        return ans
