class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = set()
        seen_pos = defaultdict(int)
        if len(fruits) == 1:
            return 1
        seen.add(fruits[0])
        seen_pos[fruits[0]] = 0
        l = 0
        mx = -999
        for r in range(1, len(fruits)):
            if fruits[r] not in seen:
                if len(seen) >= 2:
                    seen = set()
                    seen.add(fruits[r - 1])
                    seen.add(fruits[r])
                    for f, pos in seen_pos.items():
                        if f not in seen:
                            l = pos + 1
                            fruit_to_del = f
                    del seen_pos[fruit_to_del]
                    seen_pos[fruits[r]] = r
                # else:
            seen_pos[fruits[r]] = r
            seen.add(fruits[r])
            # print(seen, seen_pos, l, r)
            mx = max(mx, r - l + 1)
        return mx
