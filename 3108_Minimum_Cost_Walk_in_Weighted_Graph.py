class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def bfs(node, group, cost):
            q = deque()
            q.append(node)
            result = cost

            while q:
                node = q.popleft()
                groups[node] = group
                for nghbr, w in graph[node]:
                    if not visited[nghbr]:
                        result &= w
                        q.append(nghbr)
                visited[node] = 1
            return result

        groups = defaultdict(int)
        groups_cost = []
        visited = [0] * n
        group = 0
        for i in range(n):
            if not visited[i]:
                groups_cost.append(bfs(i, group, 2 ** 31 - 1))
                group += 1
        # for u,v in query:
        # print(groups)
        return [-1 if groups[u] != groups[v] else groups_cost[groups[u]] for u, v in query]
# class Solution:
#     def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

#         # DSU Structure
#         parent = [i for i in range(n)]
#         size = [1]*n
#         AND = [(1<<(31))-1]*n

#         def root(u):
#             if u == parent[u]:
#                 return u
#             parent[u] = root(parent[u])
#             return parent[u]

#         def union_by_size(u,v,w):

#             u = root(u)
#             v = root(v)

#             if u == v:
#                 AND[u]&=w
#                 return

#             if size[u]<size[v]:
#                 (u,v) = (v,u)

#             size[u]+=size[v]
#             parent[v] = u
#             AND[u]=AND[u]&AND[v]&w
#         # End of DSU

#         for u,v,w in edges:
#             union_by_size(u,v,w)

#         ans = []
#         for u,v in query:
#             if u == v:
#                 ans.append(0)
#             elif root(u) == root(v):
#                 ans.append(AND[root(u)])
#             else:
#                 ans.append(-1)

#         return ans
