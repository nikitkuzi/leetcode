class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        if len(hBars) == 1 or len(vBars) == 1:
            return 4
        # hBars.extend([1, m+2])
        # vBars.extend([1, n+2])
        hBars.sort()
        vBars.sort()
        h = 1
        mx_h = 1

        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                h += 1
                mx_h = max(mx_h, h)
            else:
                h = 1
        v = 1
        mx_v = 1

        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                v += 1
                mx_v = max(mx_v, v)
            else:

                v = 1
        if min(mx_h, mx_v) == 1:
            return 4
        return (min(mx_h + 1, mx_v + 1)) ** 2
