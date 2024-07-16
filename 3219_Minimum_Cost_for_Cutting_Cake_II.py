class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        row = horizontalCut
        col = verticalCut
        h, v = 1,1
        cost = 0
        while row and col:
            if col[-1]>row[-1]:
                cost+=col[-1]*h
                col.pop()
                v+=1
            else:
                cost+=row[-1]*v
                row.pop()
                h+=1
        while row:
            cost+=row[-1]*v
            row.pop()
            h+=1
        while col:
            cost+=col[-1]*h
            col.pop()
            v+=1

        return cost