class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        def check(x, y):
            if x < 0 or y < 0 or x >= n or y >= n:
                return False
            return True

        self.adj = {}
        self.diag = {}
        n = len(grid)
        adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        diag = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for x in range(n):
            for y in range(n):
                sm_adj = 0
                sm_diag = 0
                for dx, dy in adj:
                    if check(x + dx, y + dy):
                        sm_adj += grid[x + dx][y + dy]
                for dx, dy in diag:
                    if check(x + dx, y + dy):
                        sm_diag += grid[x + dx][y + dy]
                self.adj[grid[x][y]] = sm_adj
                self.diag[grid[x][y]] = sm_diag

    def adjacentSum(self, value: int) -> int:
        return self.adj[value]

    def diagonalSum(self, value: int) -> int:
        return self.diag[value]

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)