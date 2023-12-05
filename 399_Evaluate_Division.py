class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def buildGraph(eq,val):
            graph = defaultdict(dict)
            for (dividend, divisor),v in zip(eq,val):
                graph[dividend][divisor] = v
                graph[divisor][dividend] = 1/v
            return graph
        def bfs(start, end, graph):
            q = deque()
            q.append((start,1.0))
            visited = set()
            while q:
                node,val = q.popleft()
                if node == end:
                    return val
                visited.add(node)
                for connected, weight in graph[node].items():
                    if connected not in visited:
                        q.append([connected,val*weight])
            return -1
        ans = []
        graph = buildGraph(equations,values)
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ans.append(-1)
            else:
                ans.append(bfs(dividend,divisor,graph))

        return ans