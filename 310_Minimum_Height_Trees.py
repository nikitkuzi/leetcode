class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        visited = [0]*n
        self.dist = 0
        self.first_node = 0
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = deque([node for node in range(n) if len(graph[node]) == 1])

        while n>2:
            count = len(leaves)
            n-=count
            for i in range(count):
                leaf = leaves.popleft()
                for nghb in graph[leaf]:
                    graph[nghb].remove(leaf)
                    if len(graph[nghb])==1:
                        leaves.append(nghb)

        return list(leaves)