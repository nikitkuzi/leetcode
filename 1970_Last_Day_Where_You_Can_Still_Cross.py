class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def check(x, y):
            return 0 <= x < row and 0 <= y < col

        wat = defaultdict(set)

        moves = [
            [0, 1], [-1, 1], [1, 1],
            [1, 0], [-1, 0],
            [-1, -1], [1, -1], [0, -1]
        ]

        def solve():
            if 0 not in wat:
                return False

            seen = set()
            q = deque((x, 0) for x in wat[0])

            while q:
                x, y = q.popleft()
                if (x, y) in seen:
                    continue

                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if check(nx, ny) and ny in wat and nx in wat[ny]:
                        if ny == col - 1:
                            return True
                        q.append((nx, ny))

                seen.add((x, y))

            return False

        def add_day(i):
            r, c = cells[i]
            wat[c - 1].add(r - 1)

        def remove_day(i):
            r, c = cells[i]
            wat[c - 1].remove(r - 1)
            if not wat[c - 1]:
                del wat[c - 1]

        cur = 0

        def check_mid(mid):
            nonlocal cur

            while cur < mid:
                add_day(cur)
                cur += 1

            while cur > mid:
                cur -= 1
                remove_day(cur)

            return solve()

        lo, hi = 0, len(cells)
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if check_mid(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans - 1
