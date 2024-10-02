class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = set(arr)
        s = sorted(s)
        d = {s[i]:i+1 for i in range(len(s))}
        res = []
        for i in range(len(arr)):
            res.append(d[arr[i]])
        return res
