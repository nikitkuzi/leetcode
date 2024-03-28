class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]
        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)

        def dfs(node, par):
            time = 0

            for child in adj[node]:
                if child != par:
                    child_time = dfs(child, node)
                    if child_time or hasApple[child]:
                        time += 2 + child_time

            return time

        return dfs(0, -1)