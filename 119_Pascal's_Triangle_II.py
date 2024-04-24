class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            curr_row = [1]
            for j in range(len(row) - 1):
                curr_row.append(row[j] + row[j + 1])
            curr_row.append(1)
            row = curr_row
        return row