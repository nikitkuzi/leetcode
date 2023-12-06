class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites.sort()
        # graph = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        graph = defaultdict(list)

        for ai, bi in prerequisites:
            graph[ai].append(bi)

        # print(graph)
        def bfs(node, visited, stack):
            # print(graph)
            visited[node], stack[node] = 1, 1
            # if node not in graph:
            # return False
            for nghb in graph[node]:
                if visited[nghb] == 0:
                    if bfs(nghb, visited, stack):
                        return True
                elif stack[nghb] == 1:
                    return True
            stack[node] = 0

            return False

        visited = [0] * numCourses
        stack = [0] * numCourses
        for node in range(numCourses):
            if visited[node] == 0:
                if bfs(node, visited, stack):
                    return False
        return True