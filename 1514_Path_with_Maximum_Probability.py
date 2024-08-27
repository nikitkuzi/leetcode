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