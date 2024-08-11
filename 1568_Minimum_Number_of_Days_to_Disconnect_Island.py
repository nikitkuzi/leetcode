# class Solution:
#     def minDays(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#         islands = 0
#         moves = [(0, 1), (0,-1), (1, 0), (-1, 0)]
#         edges = 0
#         mid = 0
#         def check(x,y):
#             if x < 0 or y < 0 or x >= n or y >= m:
#                 return False
#             return True
#         def check_sm(x,y):
#             sm = 0
#             for dx, dy in moves:
#                 if check(x+dx, y+dy) and grid[x+dx][y+dy]!=0:
#                     sm+=1
#             return sm
#         def dfs(x, y):
#             sm = check_sm(x, y)
#             if sm <= 1:
#                 nonlocal edges
#                 edges+=1
#             if sm >= 2:
#                 nonlocal mid
#                 mid +=1
#             grid[x][y]=10
#             for dx, dy in moves:
#                 if check(x+dx, y+dy) and grid[x+dx][y+dy] == 1:
#                     dfs(x+dx, y+dy)

#         for x in range(n):
#             for y in range(m):
#                 if grid[x][y] == 1:
#                     islands += 1
#                     if islands == 2:
#                         return 0
#                     sm = check_sm(x,y)
#                     if sm <= 1:
#                         edges+=1
#                     if sm >= 2:
#                         mid+=1
#                     grid[x][y]=10
#                     for dx, dy in moves:
#                         if check(x+dx, y+dy) and grid[x+dx][y+dy] == 1:
#                             dfs(x+dx, y+dy)
#         # print(islands, edges, mid)
#         if islands == 0:
#             return 0
#         elif mid >= 1 and edges > 1:
#             return 1
#         elif edges == 1 or edges > 2:
#             return 1
#         else:
#             return 2
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands():
            seen = set()

            def dfs(r, c):
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (
                        nx, ny) not in seen:
                            seen.add((nx, ny))
                            stack.append((nx, ny))

            islands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in seen:
                        islands += 1
                        seen.add((i, j))
                        dfs(i, j)
            return islands

        if count_islands() != 1:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        return 2
