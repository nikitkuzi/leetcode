# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         def find(num):
#             if parents[num] != num:
#                 return find(parents[num])
#             return num

#         def union(prev, new_parent):
#             p1 = find(prev)
#             p2 = find(new_parent)
#             parents[p1] = p2

#         def combine(group):
#             for i, array in group.items():
#                 # print(i, array)
#                 first = array[0]
#                 for x in array[1:]:
#                     if parents[x] == x:
#                         parents[x] = find(first)
#                     else:
#                         union(first, parents[x])

#         x_group = defaultdict(list)
#         y_group = defaultdict(list)
#         parents = list(range(len(stones)))
#         for i, stone in enumerate(stones):
#             x_group[stone[0]].append(i)
#             y_group[stone[1]].append(i)
#         # print(x_group)
#         # print(y_group)
#         combine(x_group)
#         combine(y_group)
#         # print(parents)


#         for i in range(len(parents)):
#             # print(i, parents[i], find(i))
#             if parents[i] != i:
#                 # union(i, parents[i])
#                 parents[i] = parents[parents[i]]
#         for i in range(len(parents)-1, -1, -1):
#             # print(i, parents[i], find(i))
#             if parents[i] != i:
#                 # union(i, parents[i])
#                 parents[i] = parents[parents[i]]
#         for i in range(len(parents)):
#             # print(i, parents[i], find(i))
#             if parents[i] != i:
#                 # union(i, parents[i])
#                 parents[i] = parents[parents[i]]
#         # print(parents)
#         res = Counter(parents)

#         return len(stones) - len(res)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # To store the graph connections
        graph = {}

        # Build the graph
        for x, y in stones:
            if x not in graph:
                graph[x] = []
            if ~y not in graph:
                graph[~y] = []
            graph[x].append(~y)
            graph[~y].append(x)

        # To track visited nodes
        visited = set()

        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        # Counting connected components
        components = 0
        for x, y in stones:
            if x not in visited:
                dfs(x)
                components += 1

        # The number of stones that can be removed is total stones minus the number of connected components
        return len(stones) - components