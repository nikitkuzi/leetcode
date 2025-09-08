class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        x1 = n
        x2 = 0
        m = 1
        while n > 1:
            steal = 1
            if (n - steal) % 10 == 0:
                steal += 1
            x1 -= steal * m
            x2 += steal * m
            n = (n - steal) // 10
            m *= 10

        return [x1, x2]
