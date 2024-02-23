class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def f(n):
            if n == 0:
                return 0
            elif n <=2:
                return 1
            else:
                return f(n-3)+f(n-2) +f(n-1)
        return f(n)