class Solution:
    def fractionAddition(self, expression: str) -> str:
        spl = expression.split("/")
        exp = [[0,0] for i in range(len(spl)-1)]
        exp[0][0] = int(spl[0])
        exp[-1][1] = int(spl[-1])
        for i in range(1,len(spl)-1):
            if spl[i][:2] == '10':
                exp[i-1][1] = 10
                exp[i][0] = int(spl[i][2:])
            else:
                exp[i-1][1] = int(spl[i][0])
                exp[i][0] = int(spl[i][1:])
        # print(exp)
        # den = lcm(*[a[1] for a in exp])
        den = 1
        for i in range(len(exp)):
            den *= exp[i][1]
        # print(den)
        num = 0
        for i in range(len(exp)):
            exp[i][0] *= (den // exp[i][1])
            num += exp[i][0]
        # print(exp)
        # num = sum([a[0] for a in exp])
        if num % den == 0:
            return str(num//den)+"/1"
        gc = gcd(num, den)
        return str(num//gc)+"/"+str(den//gc)

