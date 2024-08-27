# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
#                        end_node: int) -> float:
#         graph = defaultdict(list)
#         for i,edge in enumerate(edges):
#             u,v = edge
#             graph[u].append((v, succProb[i]))
#             graph[v].append((u, succProb[i]))
#         visited = set()
#         dist = [0] * n
#         # @cache
#         def f(node, curr):
#             # visited.add(node)
#             for nghb, prob in graph[node]:
#                 if dist[nghb] < log(curr) + log(prob):
#                     dist[nghb] = log(curr) + log(prob)
#                     # if nghb not in visited:
#                     f(nghb, log(curr) + log(prob))
#                     # visited.add(nghb)
#         f(start_node, 1)
#         return dist[end_node]
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dist = [0] * n
        dist[start] = 1

        for _ in range(n - 1):
            updated = False
            for i, (u, v) in enumerate(edges):
                if dist[u] * succProb[i] > dist[v]:
                    dist[v] = dist[u] * succProb[i]
                    updated = True
                if dist[v] * succProb[i] > dist[u]:
                    dist[u] = dist[v] * succProb[i]
                    updated = True
            if not updated:
                break

        return dist[end]


# n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
class Solution:
    def dijkstras(self, graph, start, end):
        visited = set()
        heap = [(-1, start)]

        while heap:
            val, node = heappop(heap)
            val = -val

            if node == end:
                return val

            if node in visited:
                continue

            visited.add(node)
            for neigh_val, neigh_node in graph[node]:
                if neigh_node not in visited:
                    heappush(heap, (-val * neigh_val, neigh_node))

        return 0

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        '''
        1 path = use dijkstras
        '''
        dict_graph = defaultdict(list)

        for e in range(len(edges)):
            i, j = edges[e]
            k = succProb[e]

            dict_graph[i].append((k, j))
            dict_graph[j].append((k, i))

        return self.dijkstras(dict_graph, start_node, end_node)