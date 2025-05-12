class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            a = num // 100
            b = num // 10 % 10
            d = num % 10
            c[a] -= 1
            c[b] -= 1
            c[d] -= 1
            if c[a] >= 0 and c[b] >= 0 and c[d] >= 0:
                res.append(num)
            c[a] += 1
            c[b] += 1
            c[d] += 1
        return res
