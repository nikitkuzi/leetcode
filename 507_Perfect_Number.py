class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sm = 0
        if num == 1:
            return False
        for k in range(1, int(num**0.5)+1):
            if num % k == 0:
                sm += k
                sm += num // k
                if k == num// k or k == 1:
                    sm -= num//k
        return sm == num