class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        from collections import defaultdict
        remainder_count = defaultdict(int)
        count = 0
        for hour in hours:
            remainder = hour % 24
            if remainder == 0:
                count += remainder_count[0]
            else:
                count += remainder_count[24 - remainder]
            remainder_count[remainder] += 1
        return count