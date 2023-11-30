class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = 0
        ans = [[] for r in range(numRows)]
        visited = 0
        n = len(s)
        i = 0
        ind = 0
        if numRows == 1:
            return s
        if numRows > 2:
            d = numRows - 2
        while visited < n:
            while i < numRows + d:
                if i + ind > n - 1:
                    for i in range(numRows):
                        ans[i] = ''.join(ans[i])
                    return ''.join(ans)
                if i < numRows:
                    ans[i].append(s[i + ind])
                else:
                    ans[numRows + d - i].append(s[i + ind])
                visited += 1
                i += 1
            i = 0
            ind += numRows + d
        for i in range(numRows):
            ans[i] = ''.join(ans[i])
        return ''.join(ans)


test = Solution()
s = "PAYPALISHIRING"
# s = "A"
numRows = 3
print(test.convert(s, numRows))
