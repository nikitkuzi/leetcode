class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        one = []
        two = []
        sm = 0
        for n in nums:
            if n % 3 == 1:
                one.append(n)
            elif n % 3 == 2:
                two.append(n)
            sm += n
        if sm % 3 == 0:
            return sm
        one.sort(reverse=True)
        two.sort(reverse=True)
        # print(one)
        # print(two)
        res = []
        a = 0
        b = 0
        c = 0
        d = 0
        if len(two) >= 2:
            res.append(sm - two[-1] - two[-2])
        if two:
            res.append(sm - two[-1])
        if len(one) >= 2:
            res.append(sm - one[-1] - one[-2])
        if one:
            res.append(sm - one[-1])
        res.sort()
        # print(res)
        for n in res[::-1]:
            if n % 3 == 0:
                return n


