class Solution:
    def maximumSwap(self, num: int) -> int:
        d = defaultdict(list)
        noswap = True
        prev = '9'
        n = str(num)
        for i, c in enumerate(n):
            d[c].append(i)
            if c > prev:
                noswap = False
            prev = c
        # print(d)
        if noswap:
            return num
        mx = int(max(d.keys()))
        l = 0
        while n[l] == mx:
            l += 1
        # print(l)
        while l < len(n):
            # print(l)
            for dig in range(mx, int(n[l]), -1):
                # print(dig)
                dig = str(dig)
                if dig in d:
                    for pos in reversed(d[dig]):
                        # print(pos)
                        if pos <= l:
                            break
                        else:
                            swap = pos

                            return int(n[:l] + n[swap] + n[l + 1:swap] + n[l] + n[swap + 1:])
            # print("end")
            l += 1
