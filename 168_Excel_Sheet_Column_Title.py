class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber, rem = divmod(columnNumber, 26)
            if rem == 0:
                columnNumber -= 1
            res.append(string.ascii_uppercase[rem-1])
        res.reverse()
        return "".join(res)