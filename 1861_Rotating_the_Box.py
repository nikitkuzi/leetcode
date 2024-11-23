class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box)
        m = len(box[0])
        res = [["." for i in range(n)] for j in range(m)]
        for i in range(n):
            stones = 0
            for j in range(m):
                if box[i][j] == '#':
                    stones+=1
                if box[i][j] == '*':
                    res[j][-i-1] = '*'
                    for k in range(j-1, j-stones-1, -1):
                        res[k][-i-1] = '#'
                    stones = 0
                elif j == m-1 and stones:
                    for k in range(j, j-stones, -1):
                        res[k][-i-1] = '#'
                    stones = 0
        return res
