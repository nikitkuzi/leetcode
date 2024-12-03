class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[v][u] = w
            graph[u][v] = w

        @cache
        def dp(v=0, p=-1, in_edge=0):
            benefits = []
            total = 0
            for u in graph[v]:
                if u != p:
                    skip = dp(u, v, 0)
                    take = dp(u, v, 1) + graph[v][u]
                    total += skip
                    if take > skip:
                        benefits.append(take - skip)
            return total + sum(sorted(benefits, reverse=True)[:k - in_edge])

        ans = dp()
        dp.cache_clear()
        return ans