# class Solution:
#     def mctFromLeafValues(self, arr: List[int]) -> int:
#         n = len(arr)
#         dp = [[float('inf') for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = 0

#         for l in range(2, n + 1):
#             for i in range(n - l + 1):
#                 j = i + l - 1
#                 for k in range(i, j):
#                     rootVal = max(arr[i:k+1]) * max(arr[k+1:j+1])
#                     dp[i][j] = min(dp[i][j], rootVal + dp[i][k] + dp[k + 1][j])
#         return dp[0][n - 1]

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [inf]
        res = 0
        for num in arr:
            while stack and stack[-1] <= num:
                cur = stack.pop()
                if stack:
                    res += cur * min(num, stack[-1])
            stack.append(num)
        # print(stack)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
    hash()