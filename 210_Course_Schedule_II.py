class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for ai, bi in prerequisites:
            graph[ai].append(bi)

        visited = [False] * numCourses
        stack = [False] * numCourses
        ans = []
        self.cycle = False

        def top_sort(node, visited, ans, stack):

            visited[node] = True
            stack[node] = True
            # print(node,visited,stack)
            for n in graph[node]:
                # print(n,visited,stack)
                if not visited[n]:
                    top_sort(n, visited, ans, stack)
                elif stack[n]:
                    self.cycle = True
                    # print("asdasdasd")
            ans.append(node)
            stack[node] = False
            # print("++++")

        for course in range(numCourses):
            if not visited[course]:
                top_sort(course, visited, ans, stack)
        # print(ans,self.cycle)
        if self.cycle:
            return []
        return ans