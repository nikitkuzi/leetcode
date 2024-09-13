class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0] * (len(arr) + 1)
        pref[1] = arr[0]
        res = []
        for i in range(2, len(arr) + 1):
            pref[i] = pref[i - 1] ^ arr[i - 1]
        for l, r in queries:
            res.append(pref[r + 1] ^ pref[l])
        return res
