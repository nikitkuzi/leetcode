class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def djikstra(source):
            dist = [float("inf")] * n
            dist[source] = 0
            q = [(0, source)]
            while q:
                current_dist, node = heappop(q)
                if dist[node] == current_dist:
                    for v, w in graph[node]:
                        if current_dist + w < dist[v]:
                            dist[v] = current_dist + w
                            heappush(q, (current_dist + w, v))
            return dist

        dist0 = djikstra(0)
        dist1 = djikstra(n - 1)
        if dist0[n - 1] == float("inf"): return [False] * len(edges)
        ans = []
        for u, v, w in edges:
            ans.append(dist0[u] + w + dist1[v] == dist0[n - 1] or dist0[v] + w + dist1[u] == dist0[n - 1])
        return ans