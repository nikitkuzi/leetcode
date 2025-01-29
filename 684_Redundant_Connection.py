class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        degree = [0]*(len(edges) + 1)
        leaves = deque()
        graph = defaultdict(set)
        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
            graph[v].add(u)
            graph[u].add(v)
        for i in range(1, (len(edges)+1)):
            if degree[i] == 1:
                leaves.append(i)
        # print(leaves)
        while leaves:
            # print(leaves)
            curr = leaves.popleft()
            for nghb in graph[curr]:
                graph[nghb].remove(curr)
            if len(graph[nghb]) == 1:
                leaves.append(nghb)
            graph.pop(curr)
        # print(graph)
        for i in range(len(edges)-1, -1, -1):
            u, v = edges[i]
            if v in graph[u]:
                return [u,v]