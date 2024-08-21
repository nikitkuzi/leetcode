class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = []

        def bfs():
            visited = set()
            q = deque()
            q.append([0, 0])
            while q:
                node, dist = q.popleft()
                if node == (n - 1):
                    return dist
                visited.add(node)
                for nghb in graph[node]:
                    if nghb not in visited:
                        q.append([nghb, dist + 1])

        for i in range(n - 1):
            graph[i].append(i + 1)
            graph[i + 1].append(i)
        for u, v in queries:
            graph[u].append(v)
            graph[v].append(u)
            res.append(bfs())
        return res