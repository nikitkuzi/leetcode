class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()

        while pq:
            max_d, r, c = heapq.heappop(pq)
            if (r, c) in seen: continue
            seen.add((r, c))
            if r == m - 1 and c == n - 1:
                return max_d

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    new_d = max(max_d, grid[nr][nc])
                    heapq.heappush(pq, (new_d, nr, nc))

        return -1
# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         def check(x, y):
#             return x >= 0 and y >= 0 and x < n and y < n

#         moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         visited = [[inf for i in range(n)] for j in range(n)]
#         res = inf
#         # visited[0][0] = grid[0][0]
#         def get_nghb(x,y):
#             g_nghb = []
#             # v_nghb = []
#             for dx, dy in moves:
#                 nx = dx+x
#                 ny = dy + y
#                 if check(nx, ny):
#                     g_nghb.append((grid[nx][ny], (nx, ny)))
#                     # v_nghb.append((visited[nx][ny], (nx, ny)))
#             # return sorted(g_nghb), sorted(v_nghb)
#             # return sorted(g_nghb + v_nghb)
#             return sorted(g_nghb)

#         def traverse(x, y, t):
#             # print("in", x, y, t)
#             curr_t = t
#             nonlocal res

#             if t > res or visited[x][y] == t:
#                 # print("here1")
#                 return
#             if x == n-1 and y == n-1:
#                 res = min(res, t)
#                 # print("here2")
#                 return

#             if visited[x][y] > t:
#                 visited[x][y] = t

#             if grid[x][y] >= t:
#                 t = grid[x][y]
#             if visited[x][y] == inf:
#                 visited[x][y] = t
#             # print(x,y,t,get_nghb(x,y))
#             # for dx, dy in moves:
#             #     nx, ny = dx+x, dy+y
#             #     if not check(nx, ny):
#             #         continue
#             #     if visited[nx][ny] == inf:
#             #         traverse(nx,ny, max(t, grid[nx][ny]))
#             #     elif visited[nx][ny] > t:
#             #         traverse(nx, ny, t)

#             for gr,coords in get_nghb(x,y):
#                 nx,ny = coords[0], coords[1]
#                 if visited[nx][ny] == inf:
#                     traverse(nx,ny, max(t, gr))
#                 elif visited[nx][ny] > t:
#                     traverse(nx, ny, t)
#         traverse(0, 0, 0)

#         # for r in visited:
#         #     print(r)
#         return res
