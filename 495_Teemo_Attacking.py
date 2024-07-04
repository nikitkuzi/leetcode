class Solution:
    def findPoisonedDuration(self, A: list[int], duration: int) -> int:
        ans = 0

        for i in range(len(A) - 1):
            ans += min(duration, A[i + 1] - A[i])

        return ans + duration