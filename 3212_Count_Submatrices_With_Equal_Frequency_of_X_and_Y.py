class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res = 0
        dp = [[[0,0] for j in range(len(grid[0]))] for i in range(len(grid))]
        n = len(grid)
        m = len(grid[0])
        if grid[0][0]=="X":
            dp[0][0][0] = 1
        elif grid[0][0]=="Y":
            dp[0][0][1] = 1
        for i in range(1, n):
            dp[i][0][0]=dp[i-1][0][0]
            dp[i][0][1]=dp[i-1][0][1]
            if grid[i][0]=="X":
                dp[i][0][0] = dp[i-1][0][0]+1
            elif grid[i][0]=="Y":
                dp[i][0][1] = dp[i-1][0][1]+1
            if dp[i][0][0]==dp[i][0][1] and dp[i][0][0]> 0:
                res+=1
        for j in range(1, m):
            dp[0][j][0]=dp[0][j-1][0]
            dp[0][j][1]=dp[0][j-1][1]
            if grid[0][j]=="X":
                dp[0][j][0] = dp[0][j-1][0]+1
            elif grid[0][j]=="Y":
                dp[0][j][1] = dp[0][j-1][1]+1
            if dp[0][j][0]==dp[0][j][1] and dp[0][j][0]> 0:
                res+=1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j][0] = dp[i-1][j][0]+dp[i][j-1][0]-dp[i-1][j-1][0]
                dp[i][j][1] = dp[i-1][j][1]+dp[i][j-1][1]-dp[i-1][j-1][1]
                if grid[i][j]=="X":
                    dp[i][j][0]+=1
                elif grid[i][j]=="Y":
                    dp[i][j][1]+=1
                if dp[i][j][0] == dp[i][j][1] and dp[i][j][0]>0:
                    res+=1
        return res