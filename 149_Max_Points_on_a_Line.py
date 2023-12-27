class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        mx = float("-inf")
        for i in range(len(points)-1):
            seen_cf = {}
            for j in range(i+1,len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                # if same point dont count
                if dx == 0 and dy == 0:
                    continue
                # if vertical line then add X coord of this line
                elif dx == 0:
                    k = float("inf")
                    b = points[j][0]
                else:
                    k = dy / dx
                    b = points[i][1] - k * points[i][0]
                if (k,b) not in seen_cf:
                    seen_cf[(k,b)] = 2
                else:
                    seen_cf[(k,b)]+=1
                mx = max(mx,seen_cf[(k,b)])
            # mx = max(mx,max(seen_cf.values()))
        return mx
