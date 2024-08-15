class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        b = {5:0, 10:0, 20:0}
        for n in bills:
            if n == 5:
                b[5]+=1
                continue
            b[n]+=1
            change = n - 5
            if change >= 10 and b[10] > 0:
                b[10] -= 1
                change -= 10
            if change >= 5:
                if change // 5 > b[5]:
                    return False
                else:
                    b[5]-=change//5
        return True
