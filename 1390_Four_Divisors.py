class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            div = [1, n]
            f = True
            for k in range(2, int(n ** 0.5) + 1):
                if n % k == 0:
                    div.append(k)
                    if k != n // k:
                        div.append(n // k)
                if len(div) > 4:
                    f = False
                    break
            if f and len(div) == 4:
                res += sum(div)
        return res