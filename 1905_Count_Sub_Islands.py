# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#         n = len(grid1)
#         m = len(grid1[0])
#         parents = [i for i in range(n * m)]
#         moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#         def find(x, y):
#             if parents[x * n + y] != x * n + y:
#                 return find(parents[x * n + y])
#             return parents[x * n + y]
#
#         # def union(x1, y1, x2, y2):
#         def union(x1, y1, parent):
#             p1 = find(x1, y1)
#             # p2 = find(x2, y2)
#             parents[p1] = parent
#
#         def check(x, y):
#             if x < 0 or y < 0 or x >= n or y >= m:
#                 return False
#             return True
#
#         def f(x, y, parent):
#             for dx, dy in moves:
#                 if check(x + dx, y + dy) and grid1[x + dx][y + dy] != 0 and parents[(x + dx) * n + y + dy] == (
#                         x + dx) * n + y + dy:
#                     union(x + dx, y + dy, parent)
#                     f(x + dx, y + dy, parent)
#
#         for x in range(n):
#             for y in range(m):
#                 if grid1[x][y] != 0 and parents[x * n + y] == x * n + y:
#                     f(x, y, x * n + y)
#
#         for i in range(n):
#             for j in range(m):
#                 print(parents[i * n + j], end=' ')
#             print()

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.num_rows, self.num_cols = len(grid2), len(grid2[0])
        total_cells = self.num_rows * self.num_cols
        self.island_root = list(range(total_cells))
        self.island_status = [0] * total_cells  # 0: unvisited, 1: valid sub-island, 2: invalid sub-island

        # Perform union for grid2
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid2[row][col] == 1:
                    current_index = row * self.num_cols + col
                    if col + 1 < self.num_cols and grid2[row][col + 1] == 1:
                        self.union_islands(current_index, current_index + 1)
                    if row + 1 < self.num_rows and grid2[row + 1][col] == 1:
                        self.union_islands(current_index, current_index + self.num_cols)

        # Mark invalid sub-islands
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    root_index = self.find_island_root(row * self.num_cols + col)
                    self.island_status[root_index] = 2  # Mark as invalid sub-island

        # Count valid sub-islands
        sub_island_count = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid2[row][col] == 1:
                    root_index = self.find_island_root(row * self.num_cols + col)
                    if self.island_status[root_index] == 0:
                        sub_island_count += 1
                        self.island_status[root_index] = 1  # Mark as counted

        return sub_island_count

    def find_island_root(self, x: int) -> int:
        if self.island_root[x] != x:
            self.island_root[x] = self.find_island_root(self.island_root[x])  # Path compression
        return self.island_root[x]

    def union_islands(self, x: int, y: int):
        root_x = self.find_island_root(x)
        root_y = self.find_island_root(y)
        if root_x != root_y:
            self.island_root[root_y] = root_x