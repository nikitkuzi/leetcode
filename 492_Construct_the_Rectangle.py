class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area ** (1 / 2)) + 1, 0, -1):

            if area % i == 0:
                return [max(i, area // i), min(i, area // i)]
