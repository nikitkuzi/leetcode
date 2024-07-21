class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c = Counter(candyType)
        return min(len(c), len(candyType)//2)