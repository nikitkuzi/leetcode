class Solution:
    def waysToReachStair(self, k: int) -> int:
        ans = 0

        @cache
        def f(current, jump, k, prev):
            # print(current, jump, k, prev)
            if current > k + 1:  # or current<0:
                return 0
            ans = 0
            if current == k:
                ans += 1

            if prev == 1:
                ans += f(current + 2 ** jump, jump + 1, k, 0)
            else:
                ans += f(current + 2 ** jump, jump + 1, k, 0) + f(current - 1, jump, k, 1)
            return ans

        return f(1, 0, k, 0)
        # return ans