class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        stretch = []
        for row in mat:
            for elem in row:
                stretch.append(elem)
        if r*c!=len(mat)*len(mat[0]):
            return mat
        res = []
        for i in range(0, r*c, c):
            res.append(stretch[i:i+c])
        return res