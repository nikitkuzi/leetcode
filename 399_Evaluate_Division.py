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


# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         seen = set()
#         graph = defaultdict(list)
#         g = defaultdict(dict)
#         for i,e in enumerate(equations):
#             graph[e[0]].append([e[1],values[i]])
#             graph[e[1]].append([e[0],1/values[i]])
#         # print(graph)

#         def f(node,curr,path):
#             if node in seen:
#                 return []
#             seen.add(node)
#             temp = []
#             for nghb,v in graph[node]:
#                 if nghb not in seen:
#                     path.append([nghb,curr*v])
#                     f(nghb,curr*v,path)
#             return path


#         for node in graph.keys():
#             g[node][node] = 1
#             seen = set()
#             nghbrs = f(node,1,[])

#             for pair in nghbrs:
#                 # print(pair)

#                 nghb,v = pair[0],pair[1]
#                 g[node][nghb] = v

#         # print(g)

#         ans = []
#         for c,d in queries:
#             if c not in g or d not in g or d not in g[c]:
#                 ans.append(-1)
#             else:
#                 ans.append(g[c][d])
#         return ans
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1. Build the Graph
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        print(graph)

        # Step 2. DFS function
        def dfs(x, y, visited):
            # neither x not y exists
            if x not in graph or y not in graph:
                return -1.0

            # x points to y
            if y in graph[x]:
                return graph[x][y]

            # x maybe connected to y through other nodes
            # use dfs to see if there is a path from x to y
            for nghbr in graph[x]:
                if nghbr not in visited:
                    visited.add(nghbr)
                    temp = dfs(nghbr, y, visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][nghbr] * temp
            return -1
            # go through each of the queries and find the value

        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
        return res
        # go through each of the queries and find the value