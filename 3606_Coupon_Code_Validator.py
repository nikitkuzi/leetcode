class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        bs = ["electronics", 'grocery', 'pharmacy', 'restaurant']
        alp = string.ascii_letters + '0123456789_'
        for c, b, a in zip(code, businessLine, isActive):
            if c and all(char in alp for char in c) and a and b in bs:
                res.append(c)
        res.sort()
        return res