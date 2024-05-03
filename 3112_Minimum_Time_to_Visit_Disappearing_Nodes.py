class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        dist = [inf]*n
        dist[0] = 0
        graph = [[] for _ in range(n)]
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        q = [[0, 0]]
        while q:
            current_node, current_time = heapq.heappop(q)
            if dist[current_node] == current_time:
                for nghbr, time_to_reach in graph[current_node]:
                    if current_time + time_to_reach < disappear[nghbr] and current_time + time_to_reach < dist[nghbr]:
                        dist[nghbr] = current_time + time_to_reach
                        heapq.heappush(q,(nghbr, dist[nghbr]))
        for i in range(1,n):
            dist[i] = -1 if dist[i] == inf else dist[i]
        return [num if num < inf else -1 for num in dist]

