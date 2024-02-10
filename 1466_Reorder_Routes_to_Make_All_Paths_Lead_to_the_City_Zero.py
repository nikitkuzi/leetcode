class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        v = set()
        graph = defaultdict(list)
        for i, j in connections:
            graph[i] += [(j, 1)]
            graph[j] += [(i, -1)]
        deq = deque([0])
        count = 0
        while deq:
            cur = deq.popleft()
            v.add(cur)
            for i, direction in graph[cur]:
                if i not in v:
                    deq.append(i)
                    if direction == 1:
                        count += direction
        return count