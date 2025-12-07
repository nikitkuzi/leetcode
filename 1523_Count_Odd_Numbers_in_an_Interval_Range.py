class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-(low if low % 2 else low+1))//2+1