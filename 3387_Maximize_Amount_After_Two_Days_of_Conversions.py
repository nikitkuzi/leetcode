class Solution:

    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]],
                  rates2: List[float]) -> float:

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        res = 1
        for i, p in enumerate(pairs1):
            s, t = p
            graph1[s].append((t, float(rates1[i])))
            graph1[t].append((s, float(1 / rates1[i])))
        for i, p in enumerate(pairs2):
            s, t = p
            graph2[s].append((t, float(rates2[i])))
            graph2[t].append((s, float(1 / rates2[i])))

        dist = defaultdict(int)
        dist[initialCurrency] = 1

        def f(graph):
            for i in range(len(graph.keys())):
                updated = False
                for node in graph.keys():
                    for t, w in graph[node]:
                        if dist[t] < dist[node] * w:
                            dist[t] = dist[node] * w
                            updated = True
                if not updated:
                    break

        f(graph1)
        f(graph2)
        return dist[initialCurrency]

