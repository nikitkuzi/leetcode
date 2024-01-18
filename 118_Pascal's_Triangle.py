class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            t = []
            for j in range(i+1):
                if j == 0 or j == i:
                    t.append(1)
                else:
                    t.append(ans[i-1][j-1]+ans[i-1][j])
            ans.append(t)
        return ans