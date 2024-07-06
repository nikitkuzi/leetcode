class Solution:
    def findPoisonedDuration(self, A: list[int], duration: int) -> int:
        ans = 0

        for i in range(len(A) - 1):
            ans += min(duration, A[i + 1] - A[i])

        return anclass Solution:
    def convertToBase7(self, n: int) -> str:
        num, s = abs(n), ''
        while num:
            num, remain = divmod(num,7)
            s = str(remain) + s
        return "-" * (n < 0) + s or "0"s + duration