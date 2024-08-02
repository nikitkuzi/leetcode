class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = sum(1 for d in details if int(d[11:13]) > 60)

        return res