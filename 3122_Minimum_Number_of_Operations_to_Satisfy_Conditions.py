class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # count the number of each column
        count = [[0 for _ in range(10)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                count[j][grid[i][j]] += 1

        # dp(j, prv): the minimun changes at column j and the right column value is prv
        @cache
        def dp(j, prv_value):
            # if we reach the last column, return 0 as we do not need to pick value.
            if j == -1:
                return 0

            result = inf
            # iterate all 10 values
            for val in range(10):
                # can't choose the same value as right hand
                if val != prv_value:
                    # column j has 'count[j][val]' val, so we need to change the remaining values to val, m - count[j][val]
                    result = min(result, m - count[j][val] + dp(j - 1, val))
            return result

        return dp(n - 1, -1)