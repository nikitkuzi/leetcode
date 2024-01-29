class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        cnt = Counter(tuple(row) for row in grid)
        for tpl in zip(*grid):
            pairs += cnt[tpl]
        return pairs