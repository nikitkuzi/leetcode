class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        ans = 1
        l = points[0][0]
        for i in range(1, len(points)):
            if points[i][0] - l > w:
                l = points[i][0]
                ans+=1
        return ans