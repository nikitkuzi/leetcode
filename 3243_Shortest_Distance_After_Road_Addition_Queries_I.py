class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for i in range(n-1):
            graph[i].add(i+1)
        dist = [i for i in range(n)]

        def f(node, curr):
            dist[node] = curr
            for nghb in graph[node]:
                if dist[nghb] > curr+1:
                    f(nghb, curr+1)
        res = []
        for u, v in queries:
            graph[u].add(v)
            if dist[u]+1 < dist[v]:
                f(v, dist[u]+1)
            res.append(dist[n-1])
        return res