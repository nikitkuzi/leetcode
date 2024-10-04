class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0]*skill[1]
        res = 0
        d = defaultdict(int)
        sm = 0
        for n in skill:
            sm+=n
            d[n]+=1
        target = sm // (len(skill)//2)
        # print(target)
        for k, v in d.items():
            if v == -1:
                continue
            if target - k not in d or target-k == -1 or v != d[target-k]:
                return -1
            if k == target/2:
                # print("here")
                res += k*k*v//2
            else:
                # print("asd")
                res += k*(target-k)*v
            d[k] = -1
            d[target-k] = -1
        return res