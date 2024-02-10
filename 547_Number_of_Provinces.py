# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         color = 1
#         visited = [0]*len(isConnected)

#         def dfs(node,color,visited):
#             if visited[node] == color:
#                 return
#             visited[node] = color
#             for nghb in range(len(isConnected[node])):
#                 if isConnected[node][nghb] and not visited[nghb]:
#                     dfs(nghb,color,visited)

#         for node in range(len(isConnected)):
#             if not visited[node]:
#                 dfs(node,color,visited)
#                 color+=1
#         return color-1

class Solution:
    def dfs(self, node, isConnected, visited):
        visited[node] = True
        for i in range(len(isConnected)):
            if (isConnected[node][i] == 1 and not visited[i]):
                self.dfs(i, isConnected, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # time: O(n^2), space: O(n^2)
        n = len(isConnected)
        nComponents = 0  # num connected components in the graph
        visited = [False for i in range(n)]

        for i in range(n):
            if (not visited[i]):
                nComponents += 1
                self.dfs(i, isConnected, visited)
        return nComponents