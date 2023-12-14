class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def f(l, r, curr):

            if len(curr) == n * 2:
                nonlocal ans
                ans.append(curr)
            if l < n:
                f(l + 1, r, curr + '(')
            if r < l:
                f(l, r + 1, curr + ')')

        f(0, 0, "")
        return ans


test = Solution()
n = 3
print(test.generateParenthesis(n))
