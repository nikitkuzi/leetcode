class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        points = [0]* len(edges)
        mx = -1
        mn = inf
        for i in range(len(edges)):
            points[edges[i]]+=i
            if mx < points[edges[i]]:
                mx = points[edges[i]]
                mn = edges[i]
            elif mx == points[edges[i]]:
                mn = min(mn, edges[i])

        return mn