import math


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        largest_value = max(candidates)
        best_count = 0
        largest_power = ceil(math.log(largest_value, 2))

        for i in range(largest_power + 1):
            cur_count = 0

            for candidate in candidates:
                if candidate & (1 << i):
                    cur_count += 1

            best_count = max(best_count, cur_count)
            if best_count == largest_power:
                return best_count

        return best_count