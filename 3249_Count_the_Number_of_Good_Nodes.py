class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*(len(edges)+1)
        res = 0
        def f(node):
            visited[node] = True
            size = 0
            children = []
            for nghb in graph[node]:
                if  not visited[nghb]:
                    size+=1
                    children.append(f(nghb))
            # print(node, size, children)
            if len(children) == 0 or len(set(children))==1:
                nonlocal res
                res+=1
                # print("here", res)
            return sum(children)+size

        f(0)
        return res
