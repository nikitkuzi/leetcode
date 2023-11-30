class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points)
        min_right = points[0][1]
        ans = 1
        if len(points) > 1:
            for b in points[1:]:
                if min_right >= b[0]:
                    min_right = min(min_right, b[1])
                else:
                    ans+=1
                    min_right = b[1]
        return ans



test = Solution()
# points = [[10,16],[2,8],[1,6],[7,12]]
# points = [[2,3],[2,3]]
points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]

print(test.findMinArrowShots(points))
