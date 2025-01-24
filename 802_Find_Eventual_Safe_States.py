# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         leaves = deque()
#         indegree = defaultdict(set)
#         for i in range(len(graph)):
#             graph[i] = set(graph[i])
#             for node in graph[i]:
#                 indegree[node].add(i)
#             if len(graph[i]) == 0:
#                 leaves.append(i)
#                 # res.append(i)
#         res = []
#         while leaves:
#             curr = leaves.popleft()
#             res.append(curr)
#             for nghb in indegree[curr]:
#                 graph[nghb].remove(curr)
#                 if len(graph[nghb]) == 0:
#                     leaves.append(nghb)
#         res.sort()
#         return res
class Solution:

    def dfs(self, graph, cur_node, visited, path_visited, safe_nodes):
        # Mark the current node as visited and part of the current path
        visited[cur_node] = True
        path_visited[cur_node] = True

        for neighbor in graph[cur_node]:
            if not visited[neighbor]:
                if self.dfs(graph, neighbor, visited, path_visited, safe_nodes):
                    return True
            elif path_visited[neighbor]:  # Cycle detected
                return True

        # If no cycle is found, the node is safe
        path_visited[cur_node] = False
        safe_nodes.add(cur_node)
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        path_visited = [False] * n
        safe_nodes = set()

        for i in range(n):
            if not visited[i]:
                self.dfs(graph, i, visited, path_visited, safe_nodes)

        # Return all safe nodes sorted in ascending order
        return sorted(safe_nodes)

