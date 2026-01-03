class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        a = u = 6  # this is for our base case of n=1

        for _ in range(2, n + 1):
            next_a = (3 * a + 2 * u) % MOD
            next_u = (2 * a + 2 * u) % MOD
            a, u = next_a, next_u

        return (a + u) % MOD